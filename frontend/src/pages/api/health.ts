import type { NextApiRequest, NextApiResponse } from "next";
import { Client as PgClient } from "pg";
import Redis from "ioredis";
import { MongoClient } from "mongodb";

type HealthResponse = {
  ok: boolean;
  services: {
    postgres: { ok: boolean; latency_ms?: number; error?: string };
    redis: { ok: boolean; latency_ms?: number; error?: string };
    mongo: { ok: boolean; latency_ms?: number; error?: string };
  };
};

export default async function handler(
  _req: NextApiRequest,
  res: NextApiResponse<HealthResponse>
) {
  const services: HealthResponse["services"] = {
    postgres: { ok: false },
    redis: { ok: false },
    mongo: { ok: false },
  };

  let overallOk = true;

  // 🟢 Postgres check
  try {
    const start = Date.now();
    const pg = new PgClient({
      connectionString: process.env.POSTGRES_URL,
    });
    await pg.connect();
    await pg.query("SELECT 1");
    await pg.end();
    services.postgres = { ok: true, latency_ms: Date.now() - start };
  } catch (err: any) {
    overallOk = false;
    services.postgres = { ok: false, error: err.message };
  }

  // 🟢 Redis check
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

  // 🟢 MongoDB check
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

  res.status(overallOk ? 200 : 500).json({
    ok: overallOk,
    services,
  });
}


