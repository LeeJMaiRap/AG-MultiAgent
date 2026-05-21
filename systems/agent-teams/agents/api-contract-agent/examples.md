# API Contract Agent Examples

## Example 1: Game Account Shop API Contract

Input:

```text
Public customers browse accounts and account detail. Admin manages accounts. Architecture uses Next.js full-stack app with account model.
```

Output outline:

```md
# API Contract

## API-001 List Accounts

Endpoint:

```text
GET /api/accounts
```

Query Params:

```json
{
  "game": "optional string",
  "status": "optional available | sold",
  "page": "optional number",
  "limit": "optional number"
}
```

Response 200:

```json
{
  "items": [
    {
      "id": "acc_123",
      "title": "Rank cao giá tốt",
      "game": "Liên Quân",
      "price": 500000,
      "status": "available",
      "thumbnailUrl": "/uploads/acc_123.jpg"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 1
  }
}
```

Validation:

- `limit` max 50
- `status` must be `available` or `sold` if provided

## API-002 Account Detail

Endpoint:

```text
GET /api/accounts/:id
```

Response 200:

```json
{
  "id": "acc_123",
  "title": "Rank cao giá tốt",
  "game": "Liên Quân",
  "price": 500000,
  "status": "available",
  "description": "Thông tin acc...",
  "imageUrls": ["/uploads/1.jpg"],
  "contact": {
    "type": "facebook",
    "value": "https://facebook.com/..."
  }
}
```

Errors:

```json
{
  "error": {
    "code": "ACCOUNT_NOT_FOUND",
    "message": "Account not found",
    "details": {}
  }
}
```

## API-003 Admin Create Account

Endpoint:

```text
POST /api/admin/accounts
```

Auth:

```text
Required: yes
Role: admin
```

Request:

```json
{
  "title": "Rank cao giá tốt",
  "game": "Liên Quân",
  "price": 500000,
  "description": "Thông tin acc...",
  "status": "available",
  "imageUrls": [],
  "contact": {
    "type": "facebook",
    "value": "https://facebook.com/..."
  }
}
```
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
API-001

## Status
Done

## Summary
Created API contract for public listing/detail and admin CRUD flows.

## Files Changed
- projects/web-ban-acc-game/02-planning/api-contract.md — endpoint contracts
- projects/web-ban-acc-game/02-planning/error-contract.md — standard error shape

## Verification
API contract quality checklist passed:
- endpoints defined
- requests/responses included
- validation/auth/errors covered
- frontend/backend/QA handoff included

## Blockers
None

## Handoff Notes
Frontend and Backend can start parallel work after PM approves ownership map.
```
