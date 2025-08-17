# **Sovren AI Tech Stack Document — Unified & Refined**

This document outlines the comprehensive tech stack for Sovren AI, detailing the specific versions, configurations, and rationale behind each technology choice. It also includes governance, performance, and operational continuity guarantees. This ensures Sovren AI is not only **technically sovereign** but **strategically unassailable**.

---

## **Frontend Frameworks**

* **React**

  * **Version:** 18.2

  * **Rationale:** Component-based architecture, efficient Virtual DOM, strong ecosystem.

  * **Configuration:** Functional components with hooks for state and side effects.

* **Next.js**

  * **Version:** 13.0

  * **Rationale:** Server-side rendering \+ static generation for speed and SEO.

  * **Configuration:** Incremental Static Regeneration (ISR) enabled, API routes integrated.

* **Tailwind CSS**

  * **Version:** 3.0

  * **Rationale:** Utility-first CSS with speed of iteration.

  * **Configuration:** Sovren-specific theme and palette enforced globally.

* **Material-UI (MUI)**

  * **Version:** 5.0

  * **Rationale:** Pre-built, enterprise-ready components following Material Design.

  * **Configuration:** Sovren branding integrated into MUI theming system.

---

## **Backend Frameworks**

* **FastAPI**

  * **Rationale:** Asynchronous, high-performance Python backend for APIs.

  * **Configuration:** OpenAPI auto-docs, Redis task queues, JWT middleware.

* **Django**

  * **Version:** 4.0

  * **Rationale:** Handles complex business logic, ORM-backed persistence.

  * **Configuration:** Isolated service handling auth workflows, admin dashboards.

---

## **Database Layer**

* **PostgreSQL**

  * **Version:** 14.0

  * **Rationale:** Enterprise-grade ACID compliance, scalability.

  * **Schema:** Normalized core schema with indexing & partitioning.

  * **Security:** Row-Level Security (RLS) enforced; column-level encryption for PII.

* **MongoDB**

  * **Version:** 5.0

  * **Rationale:** Flexible document store for unstructured data.

  * **Schema:** Optimized collections for rapid aggregation.

---

## **Authentication & Access Control**

* **Exclusive Application Portal (`apply.sovrenai.app`)**

  * Replaces generic social logins. Applications reviewed and approved by Admin/Founder only.

* **Founder Role (Master Access)**

  * Above all system roles. No MFA enforcement. Untethered access to all systems.

* **RBAC Roles:**

  * Founder → Admin → Subscriber → Guest → Beta User → IT Auditor.

  * **IT Auditor Role:** Full read-only access to all system telemetry & audit logs. Cannot modify configurations. Assigned by Founder only.

  * **Beta User Role:** 10-day full-access trial, subscription required for continuation. Auto-revoked unless payment confirmed by Day 10\.

* **Tokens:**

  * JWT (RS256), 15-minute expiry, refresh rotation, centralized revocation.

---

## **LLM & AI Model Suite**

* **Speech Recognition (ASR):** Whisper Large-v3 (self-hosted).

* **Text-to-Speech (TTS):** StyleTTS2 (sovereign deployment).

* **Core LLMs:**

  * LLaMA-3 (8B & 70B) → strategic reasoning, planning.

  * Mistral 7B \+ Mixtral 8x22B → adaptive, lightweight responses, multi-agent orchestration.

  * Sovereign fine-tunes for proprietary executive personas.

* **Embeddings:** E5-Large (sentence embeddings, retrieval optimization).

* **Guardrails:** Custom adversarial filters against prompt injection, data exfiltration, and model poisoning.

### **Performance Guarantees**

* Whisper → transcription latency ≤ 500ms median.

* LLaMA-3-70B → ≤ 700ms median at 16 concurrent sessions.

* Mixtral → adaptive scaling to thousands of simultaneous requests under GPU orchestration.

---

## **DevOps / Hosting**

* **B200 Server Infrastructure (Sovereign Hardware)**

  * NUMA-aware, NVLink multi-GPU concurrency.

  * Slurm \+ NCCL for distributed inference.

  * CI/CD pipeline: GitHub Actions → Secure Direct Deploy → B200 nodes.

* **Auxiliary AWS (Storage Only)**

  * S3/Glacier used exclusively for **daily encrypted backups**.

  * **RPO:** ≤ 24 hours. **RTO:** ≤ 4 hours.

  * **Retention Policy:**

    * Daily snapshots: retained 30 days.

    * Quarterly archives: retained 7 years.

---

## **Programming Languages**

* **Python** — AI/ML logic, backend services.

* **TypeScript** — Strict, type-safe frontend logic.

* **C++** — GPU-level optimization & inference acceleration.

---

## **Monitoring & Alerting**

* **Prometheus \+ Grafana** for metrics dashboards.

* **Sentry** for application error tracing.

* **Datadog** for distributed system monitoring.

**Alerting Policies:**

* CPU \> 85% sustained → Ops escalation.

* GPU VRAM \> 90% sustained → Automatic scaling trigger.

* API latency \> 1s (p95) → PagerDuty escalation.

* Unauthorized access attempt → Immediate Founder alert.

---

## **Non-Negotiable Code Quality Standards**

* No placeholders.

* All merges must meet performance benchmarks:

  * API p95 latency ≤ 250ms.

  * GPU inference throughput ≥ defined workload threshold.

* Security hooks enforced via CI/CD pipeline.

---

# **Appendices — Full Developer Layer**

### **Appendix A — Local Developer Setup**

`# Clone Sovren AI monorepo`  
`git clone https://github.com/adminCovern/Sovren-Final.git`  
`cd Sovren-Final`

`# Frontend`  
`cd frontend`  
`npm install`  
`npm run dev`

`# Backend`  
`cd ../backend`  
`python3 -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  
`uvicorn src.main:app --reload`

`# Database`  
`cd ../database`  
`docker-compose up -d`

`# Verify`  
`docker ps`

---

### **Appendix B — Environment Templates**

**.env.frontend**

`NEXT_PUBLIC_API_URL=https://api.sovrenai.app`  
`NEXT_PUBLIC_WS_URL=wss://api.sovrenai.app/ws`  
`NEXT_PUBLIC_STRIPE_KEY=pk_live_123456`

**.env.backend**

`DATABASE_URL=postgresql://sovren:securepass@localhost:5432/sovren_ai`  
`REDIS_URL=redis://localhost:6379/0`  
`MONGO_URI=mongodb://localhost:27017/sovren`  
`JWT_SECRET=supersecurejwtkey`  
`STRIPE_SECRET=sk_live_abcdef`

**.env.database**

`POSTGRES_USER=sovren`  
`POSTGRES_PASSWORD=securepass`  
`POSTGRES_DB=sovren_ai`  
`MONGO_INITDB_ROOT_USERNAME=sovren`  
`MONGO_INITDB_ROOT_PASSWORD=securepass`

---

### **Appendix C — Deployment Commands**

`# Frontend build`  
`cd frontend`  
`npm run build`  
`npm run start`

`# Backend build`  
`cd backend`  
`uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4`

`# Database migrations`  
`cd backend`  
`alembic upgrade head`

`# Docker full build`  
`docker-compose -f infra/docker-compose.prod.yml up --build -d`

---

### **Appendix D — CI/CD Workflow**

`name: Sovren CI/CD`  
`on:`  
  `push:`  
    `branches: [ "main" ]`  
  `pull_request:`  
    `branches: [ "main" ]`

`jobs:`  
  `build:`  
    `runs-on: ubuntu-latest`  
    `steps:`  
      `- uses: actions/checkout@v3`  
      `- uses: actions/setup-python@v4`  
        `with:`  
          `python-version: "3.11"`  
      `- run: |`  
          `cd backend`  
          `pip install -r requirements.txt`  
          `pytest`  
      `- run: |`  
          `cd frontend`  
          `npm install`  
          `npm run lint`  
          `npm run test`  
          `npm run build`  
      `- run: |`  
          `docker build -t sovren/backend:latest ./backend`  
          `docker build -t sovren/frontend:latest ./frontend`  
          `docker push sovren/backend:latest`  
          `docker push sovren/frontend:latest`

---

### **Appendix E — Monitoring Recipes**

**Prometheus Config**

`scrape_configs:`  
  `- job_name: 'backend'`  
    `static_configs:`  
      `- targets: ['backend:8000']`  
  `- job_name: 'postgres'`  
    `static_configs:`  
      `- targets: ['postgres-exporter:9187']`

**Grafana Setup**

`grafana-cli plugins install grafana-piechart-panel`

**Sentry Init**

`import sentry_sdk`  
`from sentry_sdk.integrations.fastapi import FastApiIntegration`

`sentry_sdk.init(`  
    `dsn="https://example@o0.ingest.sentry.io/0",`  
    `integrations=[FastApiIntegration()],`  
    `traces_sample_rate=1.0,`  
`)`

---

### **Appendix F — Chaos Playbook**

**Redis Outage**

`docker kill $(docker ps -q --filter "ancestor=redis:7")`

**Postgres Outage**

`docker stop sovren-postgres-primary`

**Network Partition**

`tc qdisc add dev eth0 root netem loss 50% delay 200ms`

**Chaos Policy**

`{`  
  `"targets": ["postgres", "redis", "api"],`  
  `"frequency": "5m",`  
  `"kill_probability": 0.1`  
`}`

---

### **Appendix G — Backup & Recovery**

**Daily Backup Script**

`pg_dump sovren_ai | gpg --symmetric --cipher-algo AES256 > backup_$(date +%F).sql.gpg`  
`aws s3 cp backup_$(date +%F).sql.gpg s3://sovren-backups/`

**Restore**

`gpg --decrypt backup_2025-08-15.sql.gpg | psql sovren_ai`

Retention policy enforced with lifecycle rules.

---

### 

### 

### 

### **Appendix H — Accessibility & I18N**

`module.exports = {`  
  `locales: ["en", "es", "fr", "de", "jp"],`  
  `defaultLocale: "en",`  
`}`

Translation workflow handled via i18next with version-controlled JSON dictionaries.

---

## **Conclusion**

Sovren AI’s tech stack is not only modern and performant — it is sovereign, resilient, and benchmarked against Fortune 50 \+ defense standards. With this unified blueprint, every developer, operator, and auditor is forced into alignment: **there are no weak links, no placeholders, no dependencies beyond sovereign control**.

