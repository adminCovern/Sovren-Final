# Helper PowerShell script for common dev tasks
param(
    [ValidateSet('up','down','restart','logs','backend-logs','backend-test','migrate','fe-dev','fe-build','fe-audit')]
    [string]$Task = 'up'
)

$compose = "infra\docker-compose.yml"

switch ($Task) {
  'up' { docker compose -f $compose up -d; break }
  'down' { docker compose -f $compose down; break }
  'restart' { docker compose -f $compose restart; break }
  'logs' { docker compose -f $compose logs -f; break }
  'backend-logs' { docker compose -f $compose logs -f backend; break }
  'backend-test' { docker compose -f $compose exec backend pytest -q; break }
  'migrate' { docker compose -f $compose exec backend alembic -c alembic.ini upgrade head; break }
  'fe-dev' { Set-Location frontend; npm run dev; break }
  'fe-build' { Set-Location frontend; npm run build; break }
  'fe-audit' { Set-Location frontend; npm run audit; break }
  default { Write-Host "Unknown task $Task" -ForegroundColor Red; exit 1 }
}

