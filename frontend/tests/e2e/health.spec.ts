import { test, expect } from '@playwright/test';

// Baseline e2e test: ensure homepage loads, health API responds, and live status renders

test('homepage loads and health endpoint returns ok', async ({ page, request }) => {
  await page.goto('http://localhost:3000');
  await expect(page.locator('h1')).toHaveText('Sovren AI');

  // Health API
  const res = await request.get('http://localhost:3000/api/health');
  expect(res.ok()).toBeTruthy();
  const data = await res.json();
  expect(data).toEqual({ ok: true });

  // Visual status section should appear and list core services
  await expect(page.getByRole('heading', { name: 'Live system status' })).toBeVisible();
  // We expect the three cards to render labels
  await expect(page.locator('text=Postgres')).toBeVisible();
  await expect(page.locator('text=Redis')).toBeVisible();
  await expect(page.locator('text=MongoDB')).toBeVisible();
});

