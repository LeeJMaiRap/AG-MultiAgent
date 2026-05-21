# Project Rules: Trang Web Bán Hàng

## 1. Coding Standards

### JavaScript/Node.js
- Use ES6+ syntax
- Use const/let instead of var
- Use arrow functions where appropriate
- Use async/await instead of callbacks
- Naming: camelCase for variables/functions, PascalCase for classes/components

### React/Vue
- Functional components (React hooks)
- One component per file
- Props validation (PropTypes or TypeScript)
- Use meaningful component names
- Keep components small and focused

### CSS
- Use Tailwind CSS or Bootstrap 5
- Mobile-first approach
- Use CSS variables for colors/spacing
- Avoid inline styles
- Use BEM naming convention if not using utility classes

## 2. Git Workflow

### Branch Naming
- `feature/feature-name` for new features
- `bugfix/bug-name` for bug fixes
- `hotfix/issue-name` for urgent fixes

### Commit Message Format
```
[TYPE] Brief description

Detailed explanation if needed

- Bullet point 1
- Bullet point 2
```

Types: feat, fix, docs, style, refactor, test, chore

### PR Requirements
- Descriptive PR title
- Link to related issues
- Describe changes made
- Test locally before pushing

## 3. Testing Standards

### Manual Testing Checklist
- [ ] Test on Chrome, Firefox, Safari
- [ ] Test on mobile (375px), tablet (768px), desktop (1024px+)
- [ ] Test all user flows (browse, search, add to cart, checkout)
- [ ] Test admin flows (add product, update order)
- [ ] Test error cases (invalid input, network errors)

### Test Coverage
- Core business logic: 80%+
- UI components: Manual testing
- API endpoints: Manual testing with Postman/Insomnia

## 4. Documentation Standards

### Code Comments
- Comment complex logic
- Comment why, not what
- Keep comments up-to-date
- Use JSDoc for functions

### README Requirements
- Project description
- Installation instructions
- How to run locally
- API documentation
- Database schema
- Deployment instructions

### API Documentation
- Endpoint URL
- HTTP method
- Request parameters
- Response format
- Error codes
- Example requests/responses

## 5. Quality Gates

Before merging to main:
- [ ] Code review passed
- [ ] Manual tests passed
- [ ] No console errors
- [ ] No critical bugs
- [ ] Responsive design verified
- [ ] Performance acceptable (< 3s load time)

## 6. Change Management

### How to Request Changes
1. Create an issue describing the change
2. Discuss with team
3. Get approval from PM Agent
4. Implement change
5. Test thoroughly
6. Merge to main

### Impact Assessment
- Does it affect database schema?
- Does it affect API contracts?
- Does it affect UI/UX?
- Does it affect performance?
- Does it affect security?

## 7. Security Standards

### Password Security
- Hash passwords with bcrypt (salt rounds: 10)
- Never store plain text passwords
- Enforce strong password requirements

### Authentication
- Use JWT for API authentication
- Set appropriate token expiration (24h)
- Validate tokens on every protected endpoint

### Input Validation
- Validate all user inputs
- Sanitize inputs to prevent XSS
- Use parameterized queries to prevent SQL injection
- Validate file uploads

### HTTPS
- Use HTTPS in production
- Set secure cookies (httpOnly, secure, sameSite)

## 8. Performance Standards

### Frontend
- Initial load time: < 3 seconds
- Time to interactive: < 5 seconds
- Optimize images (use WebP, compress)
- Lazy load images below the fold
- Minify CSS/JS

### Backend
- API response time: < 500ms
- Database queries: < 100ms
- Use caching where appropriate
- Optimize database indexes

## 9. Accessibility Standards

### WCAG 2.1 Level A
- Use semantic HTML
- Add alt text to images
- Use proper heading hierarchy
- Ensure color contrast (4.5:1 for text)
- Make forms keyboard accessible
- Add ARIA labels where needed

## 10. Deployment Standards

### Pre-deployment Checklist
- [ ] All tests passed
- [ ] No console errors
- [ ] Environment variables configured
- [ ] Database migrations run
- [ ] Backup created
- [ ] Rollback plan ready

### Deployment Process
1. Deploy backend
2. Run database migrations
3. Deploy frontend
4. Smoke test
5. Monitor for errors

### Rollback Plan
- Keep previous version ready
- Document rollback steps
- Test rollback procedure
