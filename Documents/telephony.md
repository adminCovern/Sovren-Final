# SOVREN AI — TELEPHONY DOCTRINE
Platform: Telecom Integration (FreeSWITCH + Skyetel)
Filename: telephony.md

======================================================================
1. Purpose
======================================================================
This file establishes Sovren AI’s **sovereign telephony integration layer**.
It ensures inbound and outbound voice flows are dynamically mapped between Skyetel DIDs, FreeSWITCH dialplans, and Sovren AI’s Executive Persona layer.
This replaces static XML configs with **AI-driven, database-backed dynamic routing**.

======================================================================
2. DID → Executive Mapping
======================================================================
Each DID from Skyetel is assigned to a specific executive persona under Founder’s C-Suite.
Mapping is stored in Sovren AI’s DB (table: `executive_did_map`).

Example Mappings (current):
15306885012 → CFO Persona (CNAM: COVREN CFO)
15306885015 → COO Persona (CNAM: COVREN COO)
15306885017 → CTO Persona (CNAM: COVREN CTO)
15306885023 → CMO Persona (CNAM: COVREN CMO)
15306885024 → CLO Persona (CNAM: COVREN CLO)
15306885025 → CRO Persona (CNAM: COVREN CRO)
15306885034 → CHRO Persona (CNAM: COVREN CHRO)
15306885066 → COS Persona (CNAM: COVREN COS)

======================================================================
3. Inbound Call Handling
======================================================================
Step 1 — FreeSWITCH receives inbound call on DID.
Step 2 — Instead of static XML, FreeSWITCH queries Sovren AI API:
   GET /telephony/resolve?did=15306885012
Step 3 — Sovren AI responds with:
   - Executive persona to wake (e.g., CFO)
   - Voice pipeline (StyleTTS2/Voila)
   - Session security token
Step 4 — FreeSWITCH hands session to Sovren AI persona channel.
Step 5 — Sovren AI assumes live call as the mapped executive.

======================================================================
4. Outbound Call Handling
======================================================================
Step 1 — Sovren AI initiates outbound call on behalf of an executive.
Step 2 — Sovren AI selects the correct DID from `executive_did_map`.
   Example: CFO Persona → 15306885012.
Step 3 — Outbound call leaves Skyetel trunk with DID + CNAM (“COVREN CFO”).
Step 4 — Recipient sees correct executive identity (authoritative masking).

======================================================================
5. Dynamic Dialplan Logic
======================================================================
- FreeSWITCH configured with a **universal dialplan**:
   <extension name="dynamic">
     <condition field="destination_number" expression="^(\d+)$">
       <action application="http_request" data="http://localhost:8000/telephony/resolve?did=$1"/>
     </condition>
   </extension>

- This ensures *every inbound call* resolves dynamically via Sovren AI.
- No manual XML entries per DID.
- Scales indefinitely as new executives are added.

======================================================================
6. Skyetel Integration
======================================================================
- Skyetel trunk already provisioned.
- Sovren AI uses Skyetel API for DID pool management.
- Any new DID assigned is automatically inserted into `executive_did_map`.

======================================================================
7. Demo Mode (Founder-Only)
======================================================================
- Only Founder-level C-Suite is active initially.
- All inbound/outbound calls tied exclusively to Founder’s executive set.
- Enables live demo of Sovren AI executive orchestration:
   - Public IVR via Toll-Free.
   - Private executive personas via Local DIDs.

======================================================================
8. Success Criteria
======================================================================
- Toll-Free IVR remains live and untouched.
- Inbound calls to local DIDs reach the correct Sovren AI executive persona.
- Outbound calls from Sovren AI display correct DID + CNAM.
- No manual dialplan edits required; fully AI-driven.

======================================================================
9. Implemented Artifacts (This Repo)
======================================================================
- Database table: executive_did_map (did, persona, cnam)
- API: GET /telephony/resolve?did=E164 → { ok, persona, cnam, token }
- JWT: short-lived (5 min), HS256 using JWT_SECRET
- Seeded DIDs (Founder C-Suite): 15306885012, 15306885015, 15306885017, 15306885023, 15306885024, 15306885025, 15306885034, 15306885066
- Local FreeSWITCH dialplan example points to http://localhost:8000/telephony/resolve

- Founder instance is demo-ready for prospects.

======================================================================
END OF FILE — TELEPHONY DOCTRINE
======================================================================
