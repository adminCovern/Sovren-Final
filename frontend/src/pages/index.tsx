import Head from 'next/head';
import { useEffect, useState } from 'react';

type ServiceKey = 'postgres' | 'redis' | 'mongo';

type ServiceState = { ok: boolean; latency_ms?: number; error?: string };

type Status = { ok: boolean; services: Record<ServiceKey, ServiceState> };

function Pill({ ok, text }: { ok: boolean; text: string }) {
  return (
    <span className={`pill ${ok ? 'ok' : 'fail'}`}>
      <span className="dot" /> {text}
      <style jsx>{`
        .pill { display: inline-flex; align-items: center; gap: 8px; padding: 6px 10px; border-radius: 999px; font-weight: 600; }
        .pill.ok { background: #e7f7ec; color: #0f7b2b; border: 1px solid #bfe8c9; }
        .pill.fail { background: #fdecec; color: #9b1c1c; border: 1px solid #f5b5b5; }
        .dot { width: 8px; height: 8px; border-radius: 50%; background: currentColor; display: inline-block; }
      `}</style>
    </span>
  );
}

function Card({ name, state }: { name: string; state?: ServiceState }) {
  const ok = !!state?.ok;
  return (
    <div className="card">
      <div className="card-header">
        <strong>{name}</strong>
        <Pill ok={ok} text={ok ? 'OK' : 'FAIL'} />
      </div>
      <div className="card-body">
        {state?.latency_ms !== undefined && <div className="kv"><span>Latency</span><span>{state.latency_ms} ms</span></div>}
        {state?.error && <div className="err">{state.error}</div>}
      </div>
      <style jsx>{`
        .card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 14px; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
        .card-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
        .card-body { font-size: 14px; color: #374151; }
        .kv { display: flex; justify-content: space-between; margin-top: 6px; }
        .err { color: #9b1c1c; font-size: 13px; margin-top: 6px; word-break: break-word; }
      `}</style>
    </div>
  );
}

export default function Home() {
  const [status, setStatus] = useState<Status | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [ts, setTs] = useState<string>('');

  const load = async () => {
    try {
      const r = await fetch('/api/status', { cache: 'no-store' });
      const data = (await r.json()) as Status;
      setStatus(data);
      setErr(null);
      setTs(new Date().toLocaleTimeString());
    } catch (e: any) {
      setErr(e?.message ?? 'Failed to load status');
    }
  };

  useEffect(() => {
    load();
    const id = setInterval(load, 10000);
    return () => clearInterval(id);
  }, []);

  return (
    <>
      <Head>
        <title>Sovren AI</title>
      </Head>
      <main>
        <header className="hero">
          <h1>Sovren AI</h1>
          {status && <Pill ok={status.ok} text={status.ok ? 'All systems nominal' : 'Issues detected'} />}
        </header>

        <section className="status">
          <div className="header">
            <h2>Live system status</h2>
            <button onClick={load}>Refresh</button>
          </div>
          {err && <p className="err">{err}</p>}
          {!status && !err && <p>Checking services…</p>}
          {status && (
            <div className="grid">
              <Card name="Postgres" state={status.services.postgres} />
              <Card name="Redis" state={status.services.redis} />
              <Card name="MongoDB" state={status.services.mongo} />
            </div>
          )}
          <p className="ts">{ts && `Last updated ${ts}`}</p>
        </section>
      </main>

      <style jsx>{`
        main { max-width: 900px; margin: 40px auto; padding: 0 16px; font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }
        .hero { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
        h1 { margin: 0; }
        .status .header { display: flex; align-items: center; justify-content: space-between; }
        .grid { margin-top: 16px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
        button { padding: 6px 10px; border: 1px solid #d1d5db; background: #fff; border-radius: 8px; cursor: pointer; }
        button:hover { background: #f9fafb; }
        .err { color: #9b1c1c; }
        .ts { color: #6b7280; font-size: 12px; margin-top: 10px; }
      `}</style>
    </>
  );
}

