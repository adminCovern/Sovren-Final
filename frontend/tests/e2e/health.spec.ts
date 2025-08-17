import { test, expect } from '@playwright/test';

// Baseline e2e test: ensure homepage loads and health API responds

test('homepage loads and health endpoint returns ok', async ({ page, request }) => {
  await page.goto('http://localhost:3000');
  await expect(page.locator('h1')).toHaveText('Welcome to Sovren AI');

  const res = await request.get('http://localhost:3000/api/health');
  expect(res.ok()).toBeTruthy();
  const data = await res.json();
  expect(data).toEqual({ ok: true });
});

