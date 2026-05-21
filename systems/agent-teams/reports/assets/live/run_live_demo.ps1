# PowerShell script simulating the Agent-Teams demo run
$ErrorActionPreference = "Stop"

$base = "D:\Antigravity\LeeJ_MultiAgent\systems\agent-teams\reports\assets\live"
$logs = Join-Path $base "logs"

if (!(Test-Path $logs)) {
    New-Item -ItemType Directory -Path $logs -Force | Out-Null
}

$reqLog = Join-Path $logs "requirements.log"
$beLog = Join-Path $logs "backend.log"
$qaLog = Join-Path $logs "qa.log"
$timelineLog = Join-Path $logs "timeline.log"

# Clean up old logs if they exist
Clear-Content -Path $reqLog -ErrorAction SilentlyContinue
Clear-Content -Path $beLog -ErrorAction SilentlyContinue
Clear-Content -Path $qaLog -ErrorAction SilentlyContinue
Clear-Content -Path $timelineLog -ErrorAction SilentlyContinue

$now = { (Get-Date -Format "yyyy-MM-ddTHH:mm:ss") }

# 1. Requirements Agent
Write-Host "[Requirements Agent] Starting..." -ForegroundColor Cyan
Add-Content -Path $reqLog -Value "[Requirements Agent] ACK demo-2026-05-20-1533 at $(&$now)"
Add-Content -Path $timelineLog -Value "[PM] REQ ACK at $(&$now)"
Start-Sleep -Seconds 2

Write-Host "[Requirements Agent] Creating handoff..." -ForegroundColor Cyan
Add-Content -Path $reqLog -Value "[Requirements Agent] WORKING scope: TODO CLI add/list at $(&$now)"
$handoffReqToBe = @"
# Handoff REQ -> BE
- Build tiny TODO CLI local-only
- Commands: add <text>, list
- Storage: JSON local file
"@
$handoffReqToBe | Out-File -FilePath (Join-Path $base "handoff-req-to-be.md") -Encoding utf8
Add-Content -Path $reqLog -Value "[Requirements Agent] DONE handoff-req-to-be.md at $(&$now)"
Add-Content -Path $timelineLog -Value "[PM] REQ -> BE handoff ready at $(&$now)"
Start-Sleep -Seconds 2

# 2. Backend Agent
Write-Host "[Backend Agent] Starting..." -ForegroundColor Yellow
Add-Content -Path $beLog -Value "[Backend Agent] ACK demo-2026-05-20-1533 at $(&$now)"
Add-Content -Path $beLog -Value "[Backend Agent] WORKING implement todo-mini.js at $(&$now)"

$todoMiniJs = @"
#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const p = path.join(__dirname, 'todo-mini.json');
const [,,cmd,...args]=process.argv;
const load=()=>fs.existsSync(p)?JSON.parse(fs.readFileSync(p,'utf8')):[];
const save=(d)=>fs.writeFileSync(p,JSON.stringify(d,null,2));
const d=load();
if(cmd==='add'){
    const t=args.join(' ').trim();
    if(!t){
        console.error('ERR missing text');
        process.exit(1);
    }
    d.push({id:d.length+1,text:t});
    save(d);
    console.log('OK add');
}
else if(cmd==='list'){
    if(!d.length) console.log('EMPTY');
    else d.forEach(x=>console.log(`\${x.id}. \${x.text}`));
}
else{
    console.log('USAGE add <text> | list');
    process.exit(1);
}
"@
$todoMiniJs | Out-File -FilePath (Join-Path $base "todo-mini.js") -Encoding utf8

$handoffBeToQa = @"
# Handoff BE -> QA
- CLI path: D:\Antigravity\LeeJ_MultiAgent\systems\agent-teams\reports\assets\live\todo-mini.js
- Please run add/list positive and negative tests
"@
$handoffBeToQa | Out-File -FilePath (Join-Path $base "handoff-be-to-qa.md") -Encoding utf8
Add-Content -Path $beLog -Value "[Backend Agent] DONE todo-mini.js + handoff-be-to-qa.md at $(&$now)"
Add-Content -Path $timelineLog -Value "[PM] BE -> QA handoff ready at $(&$now)"
Start-Sleep -Seconds 2

# 3. QA Agent
Write-Host "[QA Agent] Starting..." -ForegroundColor Green
Add-Content -Path $qaLog -Value "[QA Agent] ACK demo-2026-05-20-1533 at $(&$now)"
Add-Content -Path $qaLog -Value "[QA Agent] WORKING run tests at $(&$now)"

# Run test commands and write output to qa-report.md
$qaReportPath = Join-Path $base "qa-report.md"
$testOutput = & {
    Write-Output "== QA TEST =="
    node (Join-Path $base "todo-mini.js") list
    node (Join-Path $base "todo-mini.js") add "buy coffee"
    node (Join-Path $base "todo-mini.js") list
    try {
        node (Join-Path $base "todo-mini.js") add
    } catch {
        Write-Output "Negative test caught error"
    }
}
$testOutput | Out-File -FilePath $qaReportPath -Encoding utf8

Add-Content -Path $qaLog -Value "[QA Agent] DONE qa-report.md at $(&$now)"
Add-Content -Path $timelineLog -Value "[PM] QA done. Demo complete at $(&$now)"

Write-Host "Demo run completed successfully!" -ForegroundColor Green
