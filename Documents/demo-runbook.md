# Sovren AI — Demo Runbook (Founder‑Friendly)

Use this checklist to bring the system up, verify it live, and (optionally) manage telephony DIDs. Copy/paste commands as shown. Everything runs locally unless noted.

---

## 0) Prerequisites
- Docker Desktop running
- PowerShell (Windows) or WSL/Git Bash
- Node.js 18+ for the frontend dev server

Repo root path (PowerShell):
- Set-Location "C:\Users\brian\OneDrive - Covren Firm\Desktop\Sovren-AI-Final\Sovren-Final"

---

## 1) Start backend + databases (Docker)
- Start services:
  - docker compose -f infra/docker-compose.yml up -d
- Wait for DB to be healthy and backend to start:
  - docker compose -f infra/docker-compose.yml ps
- Tail backend logs (optional):
  - docker compose -f infra/docker-compose.yml logs -f backend

---

## 2) Start frontend (Next.js)
- In a new PowerShell window:
  - Set-Location "C:\Users\brian\OneDrive - Covren Firm\Desktop\Sovren-AI-Final\Sovren-Final\frontend"
  - npm ci (first run only)
  - npm run dev
- Open the app:
  - start http://localhost:3000

What you should see: a homepage with a “Live system status” section showing Postgres/Redis/Mongo state (OK/FAIL) with latency.

---

## 3) Quick health checks (copy/paste)
- Backend health:
  - curl http://localhost:8000/health
- Backend service status (JSON):
  - curl http://localhost:8000/status
- Prometheus metrics (text):
  - curl http://localhost:8000/metrics | more

Expected: HTTP 200s; status JSON shows each service with ok: true when healthy.

---

## 4) Telephony resolve — verify mapping
Two ways to get a mapping:

A) Seeded Founder DIDs (already included)
- Try one:
  - curl "http://localhost:8000/telephony/resolve?did=15306885012"
- Expected: { ok: true, persona: "CFO", cnam: "COVREN CFO", token: "..." }

B) Insert or edit a DID mapping yourself
- Option 1 (Admin API; secure):
  1) Edit infra/docker-compose.yml → backend.environment: add a line
     - ADMIN_TOKEN: change-this-token
  2) Restart backend:
     - docker compose -f infra/docker-compose.yml up -d backend
  3) Upsert a mapping (replace values as needed):
     - curl -X POST "http://localhost:8000/telephony/admin/map?did=15551234567&persona=CTO&cnam=COVREN%20CTO" -H "Authorization: Bearer change-this-token"
  4) Verify:
     - curl "http://localhost:8000/telephony/resolve?did=15551234567"

- Option 2 (Direct SQL):
  - docker compose -f infra/docker-compose.yml exec db psql -U sovren -d sovren_ai -c "insert into executive_did_map(did, persona, cnam) values ('15551230000','COO','COVREN COO') on conflict (did) do update set persona=EXCLUDED.persona, cnam=EXCLUDED.cnam;"
  - curl "http://localhost:8000/telephony/resolve?did=15551230000"

Notes:
- The resolve response includes a short‑lived JWT token (5 minutes) carrying did/persona/cnam claims.

---

## 5) FreeSWITCH dialplan (local demo)
Point your inbound route to Sovren AI’s resolve endpoint:

<extension name="dynamic">
  <condition field="destination_number" expression="^(\d+)$">
    <action application="http_request" data="http://localhost:8000/telephony/resolve?did=$1"/>
  </condition>
</extension>

When moving to a remote host, change the URL host to your server’s public base URL.

---

## 6) One‑minute smoke test (PowerShell)
Run each and confirm HTTP 200 and OK states:
- curl http://localhost:8000/health
- curl http://localhost:8000/status
- curl "http://localhost:8000/telephony/resolve?did=15306885012"
- start http://localhost:3000 (visual status shows OK)

---

## 7) Troubleshooting
- Frontend port busy → use another port:
  - npm run dev -- -p 3001 → open http://localhost:3001
- Docker services not healthy:
  - docker compose -f infra/docker-compose.yml logs -f db
  - docker compose -f infra/docker-compose.yml logs -f backend
- Status shows FAIL for a service:
  - Ensure Docker is running and required ports are free
  - Try: docker compose -f infra/docker-compose.yml restart

---

## 8) Where to look next
- Documents/launch-ai.md — high-level launch sequence
- Documents/telephony.md — telephony doctrine + implemented artifacts

This runbook is kept short and task‑oriented; if anything is unclear, say “clarify step X” and I will refine it.

