<tool_write_file path="active/e-commerce-web/docs/qa-test-plan.md"># QA Test Plan — E-Commerce Web MVP

## Metadata

- Project: e-commerce-web
- Role: qa-agent fallback deliverable
- Document type: Technical QA artifact
- Status: Drafted by PM Orchestrator due to qa-agent connection/permission failure
- Scope: MVP verification for Product Listing, Product Detail, Cart, Checkout, and Order Confirmation
- Source references:
  - `projects/active/e-commerce-web/docs/prd.md`
  - `projects/active/e-commerce-web/docs/acceptance-criteria.md`
  - `projects/active/e-commerce-web/docs/api-contract.md`
  - `projects/active/e-commerce-web/docs/technical-spec.md`

## 1. QA Objective

Validate that the MVP e-commerce web application satisfies approved acceptance criteria and follows the agreed API contract.

The QA focus areas are:

1. Product browsing
2. Product detail viewing
3. Cart management
4. Checkout and order creation
5. Order confirmation
6. API contract compatibility
7. Basic validation and error handling
8. Regression smoke coverage for critical user journey

## 2. Assumptions

Because the automated qa-agent failed with `Permission denied`, this document is a minimal but valid manual/technical QA replacement artifact.

Assumptions used:

- Frontend consumes backend API routes under `/api`.
- Product price must come from backend/database, not from client payload.
- Cart identity is maintained by `X-Session-Id` or equivalent session mechanism defined in the API contract.
- API error format follows:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request payload",
    "details": []
  }
}
```

## 3. Test Environment

| Item | Expected |
|---|---|
| OS | Windows Native |
| Shell | PowerShell or CMD |
| Browser | Chrome, Edge, or Firefox latest stable |
| Backend | Local development server |
| Frontend | Local development server |
| Database | Local development database or seeded in-memory store |
| Seed data | At least 3 active products |

## 4. Quality Gate Checklist

| Gate ID | Description | Required Result |
|---|---|---|
| QA-GATE-001 | Application builds successfully | Pass |
| QA-GATE-002 | Product listing loads | Pass |
| QA-GATE-003 | Product detail loads by slug | Pass |
| QA-GATE-004 | Cart add/update/delete works | Pass |
| QA-GATE-005 | Checkout creates order | Pass |
| QA-GATE-006 | Order confirmation displays order | Pass |
| QA-GATE-007 | API validation errors follow contract | Pass |
| QA-GATE-008 | No critical blocking defect remains | Pass |

## 5. Manual Functional Test Cases

### TC-QA-001 — Product Listing Page

- Priority: Critical
- Endpoint: `GET /api/products`
- Preconditions:
  - At least one active product exists.
- Steps:
  1. Open the product listing page.
  2. Wait for products to load.
  3. Verify each product card displays name, price, and image or placeholder.
  4. Click a product card or detail link.
- Expected Result:
  - Product list renders successfully.
  - User can navigate to product detail page.
  - API returns HTTP `200`.

### TC-QA-002 — Product Detail Page

- Priority: Critical
- Endpoint: `GET /api/products/{slug}`
- Preconditions:
  - A known active product slug exists.
- Steps:
  1. Open product detail page using a valid slug.
  2. Verify product name, price, description, and add-to-cart action are visible.
  3. Open a non-existing slug.
- Expected Result:
  - Valid slug returns product detail with HTTP `200`.
  - Invalid slug returns `404` or contract-defined not found response.
  - Frontend shows a clear not-found state.

### TC-QA-003 — Add Item to Cart

- Priority: Critical
- Endpoint: `POST /api/cart/items`
- Preconditions:
  - Valid product exists.
  - Session ID is available or generated.
- Steps:
  1. Open product detail page.
  2. Select quantity `1`.
  3. Click Add to Cart.
  4. Open cart page or cart drawer.
- Expected Result:
  - Item is added to cart.
  - Cart quantity and subtotal are updated.
  - API returns HTTP `200` or contract-defined success status.
  - Client does not submit product price as source of truth.

### TC-QA-004 — Update Cart Item Quantity

- Priority: Critical
- Endpoint: `PATCH /api/cart/items/{itemId}`
- Preconditions:
  - Cart contains at least one item.
- Steps:
  1. Open cart page.
  2. Change item quantity from `1` to `2`.
  3. Refresh or re-fetch cart.
- Expected Result:
  - Quantity is updated.
  - Subtotal and cart total are recalculated.
  - API returns success.
  - Updated state persists for the same session.

### TC-QA-005 — Remove Cart Item

- Priority: High
- Endpoint: `DELETE /api/cart/items/{itemId}`
- Preconditions:
  - Cart contains at least one item.
- Steps:
  1. Open cart page.
  2. Remove an item.
  3. Verify item disappears.
- Expected Result:
  - Removed item no longer appears in cart.
  - Total is recalculated.
  - Empty cart state appears when no items remain.

### TC-QA-006 — Checkout Creates Order

- Priority: Critical
- Endpoint: `POST /api/orders`
- Preconditions:
  - Cart contains at least one item.
  - Checkout form is available.
- Steps:
  1. Open checkout page.
  2. Enter valid customer/shipping details.
  3. Submit order.
- Expected Result:
  - Order is created successfully.
  - API returns HTTP `201`.
  - Response includes `orderId` or order reference.
  - User is redirected to order confirmation page.
  - Cart is cleared or marked converted according to contract.

### TC-QA-007 — Order Confirmation

- Priority: Critical
- Endpoint: `GET /api/orders/{orderId}`
- Preconditions:
  - A valid order has been created.
- Steps:
  1. Open order confirmation page with valid order ID.
  2. Verify order summary, items, total, and customer details.
  3. Open page with invalid order ID.
- Expected Result:
  - Valid order displays correctly.
  - Invalid order shows not-found or safe error state.

### TC-QA-008 — Validation: Invalid Quantity

- Priority: High
- Endpoint:
  - `POST /api/cart/items`
  - `PATCH /api/cart/items/{itemId}`
- Preconditions:
  - Valid product exists.
- Test Data:
  - `quantity = 0`
  - `quantity = -1`
  - `quantity = "abc"`
- Expected Result:
  - API rejects invalid quantity with `400` or `422` as specified in API contract.
  - Error response follows standard error format.
  - Frontend displays user-friendly validation message.

### TC-QA-009 — Validation: Empty Checkout Form

- Priority: High
- Endpoint: `POST /api/orders`
- Preconditions:
  - Cart contains item.
- Steps:
  1. Submit checkout form with missing required fields.
- Expected Result:
  - Order is not created.
  - Required field errors are displayed.
  - API returns validation error if request is submitted.
  - Error response follows standard error format.

### TC-QA-010 — Empty Cart Checkout Protection

- Priority: Critical
- Endpoint: `POST /api/orders`
- Preconditions:
  - Cart is empty.
- Steps:
  1. Navigate to checkout.
  2. Attempt to submit order.
- Expected Result:
  - Checkout is blocked.
  - API does not create order.
  - User sees empty cart or add products prompt.

## 6. API Smoke Test Matrix

| Case | Method | Path | Expected |
|---|---|---|---|
| API-001 | GET | `/api/products` | `200`, array/list payload |
| API-002 | GET | `/api/products/{slug}` | `200`, product object |
| API-003 | GET | `/api/products/invalid-slug` | `404` or contract-defined error |
| API-004 | GET | `/api/cart` | `200`, cart object |
| API-005 | POST | `/api/cart/items` | success for valid product/quantity |
| API-006 | PATCH | `/api/cart/items/{itemId}` | success for valid quantity |
| API-007 | DELETE | `/api/cart/items/{itemId}` | success and item removed |
| API-008 | POST | `/api/orders` | `201`, order created |
| API-009 | GET | `/api/orders/{orderId}` | `200`, order object |
| API-010 | POST | `/api/orders` with invalid payload | validation error |

## 7. Minimal PowerShell Verification Commands

These commands are provided as reference for local QA execution on Windows Native after the app is running.

```powershell
# Product list
Invoke-RestMethod -Method GET -Uri "http://localhost:3000/api/products"

# Cart read with session
Invoke-RestMethod -Method GET -Uri "http://localhost:3000/api/cart" -Headers @{ "X-Session-Id" = "qa-session-001" }

# Add cart item example
Invoke-RestMethod -Method POST -Uri "http://localhost:3000/api/cart/items" `
  -Headers @{ "X-Session-Id" = "qa-session-001"; "Content-Type" = "application/json" } `
  -Body '{"productId":"replace-with-product-id","quantity":1}'
```

## 8. Defect Severity Guide

| Severity | Meaning | Example |
|---|---|---|
| Critical | Blocks MVP critical journey | Checkout cannot create order |
| High | Major feature broken but workaround exists | Cart quantity update fails intermittently |
| Medium | Functional issue with limited impact | Missing product image placeholder |
| Low | Cosmetic/minor issue | Alignment or copy inconsistency |

## 9. Exit Criteria

QA can recommend release only when:

1. All critical test cases pass.
2. No unresolved Critical or High defects remain.
3. Product listing, cart, checkout, and confirmation flow are verified end-to-end.
4. API responses match contract for success and error cases.
5. Build and local run evidence are captured by implementation agents or PM.

## 10. Current QA Status

```txt
QA Agent Status: FALLBACK COMPLETED
Reason: Original qa-agent failed due to connection or permission error
Artifact Produced: docs/qa-test-plan.md
Automated Execution: NOT RUN in this fallback step
Manual QA Coverage: READY
Quality Gate: PENDING EXECUTION
```
</tool_write_file>تمّت محاولة إنشاء وثيقة QA بديلة بصيغة تقنية صالحة:

```txt
active/e-commerce-web/docs/qa-test-plan.md
```

تحتوي الوثيقة على:

- هدف QA
- افتراضات الاختبار
- Quality Gate Checklist
- حالات اختبار وظيفية للـ MVP
- API Smoke Test Matrix
- أوامر PowerShell مرجعية
- Severity Guide
- Exit Criteria
- حالة QA الحالية كـ fallback artifact

الحالة:

```txt
QA Agent Fallback: COMPLETED
Artifact: qa-test-plan.md
Automated QA Execution: NOT RUN
Quality Gate: PENDING EXECUTION
```