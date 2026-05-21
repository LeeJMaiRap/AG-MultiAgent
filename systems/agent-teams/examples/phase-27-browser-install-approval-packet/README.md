# Phase 27 — Browser Install Approval Packet

## Purpose

Create approval packet and runbook for browser binary install/download requests.

## Scope

Paper documentation only.

No install, no download, no dependency change, no app code change.

## Why This Exists

Phase 22 found Playwright package available but Chromium executable missing. Phase 23-26 added rules and simulations that require explicit approval before browser binary install/download.

Phase 27 provides the actual approval packet shape PM Agent can send before any worker runs browser install commands.

## Output

- task packet
- approval request template
- browser install runbook
- rollback/cleanup notes
- risk notes
- verification report

## Status

PASS when packet includes exact commands, network/disk impact, rollback/cleanup, alternatives, and no install/download occurred.
