import type { NextApiRequest, NextApiResponse } from "next";
import { Client as PgClient } from "pg";
import Redis from "ioredis";
import { MongoClient } from "mongodb";

type ServiceState = { ok: boolean; latency_ms?: number; error?: string };
type StatusResponse = {
  ok: boolean;
  services: {
    postgres: ServiceState;
    redis: ServiceState;
    mongo: ServiceState;
    vllm: ServiceState;
    voice: ServiceState;
    vault: ServiceState;
    siem: ServiceState;
  };
};

export default async function handler(
  _req: NextApiRequest,
  res: NextApiResponse<StatusResponse>
) {
  const services: StatusResponse["services"] = {
    postgres: { ok: false },
    redis: { ok: false },
    mongo: { ok: false },
    vllm: { ok: false },
    voice: { ok: false },
    vault: { ok: false },
    siem: { ok: false },
  };

  let overallOk = true;

  // 🟢 Postgres
  try {
    const start = Date.now();
    const pg = new PgClient({ connectionString: process.env.POSTGRES_URL });
    await pg.connect();
    await pg.query("SELECT 1");
    await pg.end();
    services.postgres = { ok: true, latency_ms: Date.now() - start };
  } catch (err: any) {
    overallOk = false;
    services.postgres = { ok: false, error: err.message };
  }

  // 🟢 Redis
  try {
    const start = Date.now();
    const redis = new Redis(process.env.REDIS_URL!);
    await redis.ping();
    await redis.quit();
    services.redis = { ok: true, latency_ms: Date.now() - start };
  } catch (err: any) {
    overallOk = false;
    services.redis = { ok: false, error: err.message };
  }

  // 🟢 MongoDB
  try {
    const start = Date.now();
    const mongo = new MongoClient(process.env.MONGO_URL!);
    await mongo.connect();
    await mongo.db().command({ ping: 1 });
    await mongo.close();
    services.mongo = { ok: true, latency_ms: Date.now() - start };
  } catch (err: any) {
    overallOk = false;
    services.mongo = { ok: false, error: err.message };
  }

  // 🟢 vLLM Service
  try {
    const start = Date.now();
    const r = await fetch(process.env.VLLM_URL || "http://sovren-vllm-svc:8000", {
      method: "GET",
    });
    if (r.ok) {
      services.vllm = { ok: true, latency_ms: Date.now() - start };
    } else {
      throw new Error(`HTTP ${r.status}`);
    }
  } catch (err: any) {
    overallOk = false;
    services.vllm = { ok: false, error: err.message };
  }

  // 🟢 Voice Service
  try {
    const start = Date.now();
    const r = await fetch(process.env.VOICE_URL || "http://sovren-voice-svc:8000");
    if (r.ok) {
      services.voice = { ok: true, latency_ms: Date.now() - start };
    } else {
      throw new Error(`HTTP ${r.status}`);
    }
  } catch (err: any) {
    overallOk = false;
    services.voice = { ok: false, error: err.message };
  }

  // 🟢 Vault Service
  try {
    const start = Date.now();
    const r = await fetch(process.env.VAULT_URL || "http://sovren-vault-svc:8200/v1/sys/health");
    if (r.ok) {
      services.vault = { ok: true, latency_ms: Date.now() - start };
    } else {
      throw new Error(`HTTP ${r.status}`);
    }
  } catch (err: any) {
    overallOk = false;
    services.vault = { ok: false, error: err.message };
  }

  // 🟢 SIEM Service
  try {
    const start = Date.now();
    const r = await fetch(process.env.SIEM_URL || "http://sovren-siem-svc:9090");
    if (r.ok) {
      services.siem = { ok: true, latency_ms: Date.now() - start };
    } else {
      throw new Error(`HTTP ${r.status}`);
    }
  } catch (err: any) {
    overallOk = false;
    services.siem = { ok: false, error: err.message };
  }

  res.status(overallOk ? 200 : 500).json({
    ok: overallOk,
    services,
  });
}
