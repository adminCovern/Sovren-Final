import type { NextApiRequest, NextApiResponse } from 'next';

// Proxy to backend /status to ensure no placeholders
export default async function handler(_req: NextApiRequest, res: NextApiResponse) {
  try {
    const r = await fetch('http://localhost:8000/status', { cache: 'no-store' });
    const data = await r.json();
    res.status(200).json(data);
  } catch (err: any) {
    res.status(500).json({ ok: false, error: err?.message ?? 'unknown' });
  }
}

