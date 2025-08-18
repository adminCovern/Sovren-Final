# SOVREN AI — LAUNCH SEQUENCE (AI-NATIVE)
Platform: Hybrid Execution (Augment Agent in VS Code + Claude Code in Server CLI)
Filename: launch-ai.md

======================================================================
1. Purpose
======================================================================
This file replaces the deprecated `launch-ops.md`.
It defines a **fully AI-native launch sequence** that can be executed by either:
- **Augment Agent inside Visual Studio Code**, or
- **Claude Code inside the Sovren AI server CLI**.

Goal: Ensure Sovren AI boots into a **production-grade, demo-ready state** with telephony, frontend, backend, and C-Suite orchestration fully active.

======================================================================
2. Scope of Launch
======================================================================
- Backend services (B200 NVLink mesh, LLM stack, observability).
- Frontend/UI services (cinematic, sovereign presence).
- Executive orchestration layer (Founder C-Suite).
- Telephony initialization (via `telephony.md`).
- Developer acceleration loop (Augment Agent + Claude subagents).

======================================================================
3. Launch Steps
======================================================================

Step 1 — Load VS Code Tasking
- Augment Agent loads `task-vscode.md`.
- Applies accelerated codebase development mandates.
- Initializes build pipeline.

Step 2 — Dispatch Claude Subagents
- Push `subagents-claude.md` to Claude Code (Server CLI).
- Claude Code spawns required subagents:
  - Infrastructure Agent
  - Compliance/Monitoring Agents
  - Telephony Integration Agent
  - Security Hardening Agent
  - Launch Subagent (arbiter)

Step 3 — Initialize Telephony Layer
- Execute `telephony.md`.
- DID → Executive Persona mapping applied.
- FreeSWITCH dialplan updated dynamically.
- Outbound CNAM/DID masking enforced.
- Toll-Free IVR preserved.

Step 4 — Synchronize Backend + Frontend
- Backend (LLM stack, observability, security) comes online.
- Frontend/UI (React, Tailwind, Three.js cinematic layer) initialized.
- Sovren AI orchestrates full-stack integration.

Step 5 — Founder Sandbox Activation
- Only Founder-level C-Suite is live.
- Local DIDs routed to Sovren AI executive personas.
- Outbound calls masked with correct CNAM (e.g., COVREN CFO).
- Demo-ready environment enabled.

Step 6 — Validation & Reporting
- End-to-end validation tests run:
  - Voice-first latency < 200ms.
  - GPU utilization mapping active.
  - Inbound/outbound call routing confirmed.
  - UI responsiveness benchmarked.
- Augment Agent and Claude Code log telemetry to Sovren AI observability stack.

======================================================================
7. What’s Implemented in This Repo (Fast Path)
======================================================================
- Frontend: Next.js app with live status dashboard (Postgres/Redis/Mongo)
- Backend: FastAPI with /health, /status, /metrics, /telephony/resolve
- Telephony: DID map table + seeded Founder DIDs; JWT-signed resolve responses
- Infra: Docker Compose with healthchecks and dependency gating
- CI: Frontend lint/build; Backend pytest; npm audit; pip-audit

Runbook (Local Demo)
- docker compose -f infra/docker-compose.yml up -d
- Visit http://localhost:3000 (UI) and http://localhost:8000/status (JSON)
- Test telephony resolve: http://localhost:8000/telephony/resolve?did=15306885012

Owner Controls
- To add/modify DID mappings, update table executive_did_map (admin endpoint optional)


======================================================================
4. Success Criteria
======================================================================
- Sovren AI boots with **zero manual human ops**.
- Founder C-Suite telephony fully functional (inbound + outbound).
- Demo-ready environment active immediately.
- Augment Agent + Claude Code orchestration loop established.
- System validated against sovereign doctrine (security, sovereignty, performance).

======================================================================
END OF FILE — LAUNCH SEQUENCE (AI-NATIVE)
======================================================================
