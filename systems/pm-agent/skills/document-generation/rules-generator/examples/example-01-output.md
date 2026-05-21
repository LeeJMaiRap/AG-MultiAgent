# Project Rules: Hệ thống quản lý task nội bộ

## 1. Coding Standards

### JavaScript/Node.js
- Use ES6+ syntax
- Use const/let instead of var
- Use arrow functions where appropriate
- Use async/await instead of callbacks
- Naming: camelCase for variables/functions, PascalCase for classes/components

### React
- Functional components with hooks
- One component per file
- Use meaningful component names
- Keep components small and focused
- Props validation with PropTypes or TypeScript

### CSS/Tailwind
- Use Tailwind CSS utility classes
- Mobile-first approach
- Avoid inline styles
- Use consistent spacing scale

## 2. Git Workflow

### Branch Naming
- `feature/feature-name` for new features
- `bugfix/bug-name` for bug fixes
- `hotfix/issue-name` for urgent fixes

### Commit Message Format
```
[TYPE] Brief description

Detailed explanation if needed
```

Types: feat, fix, docs, style, refactor, test, chore

### PR Requirements
- Descriptive PR title
- Describe changes made
- Test locally before pushing
- Request review from at least one team member

## 3. Testing Standards

### Manual Testing Checklist
- [ ] Test tạo task
- [ ] Test phân công người thực hiện
- [ ] Test cập nhật trạng thái task
- [ ] Test comment trong task
- [ ] Test đính kèm file
- [ ] Test phân quyền admin/member
- [ ] Test responsive trên mobile và desktop
- [ ] Test error cases (invalid input, network errors)

### Test Coverage
- Core business logic: Manual testing cho MVP
- API endpoints: Manual testing với Postman/Insomnia
- UI flows: Manual testing trên browser

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
- Environment variables

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
- [ ] Documentation updated

## 6. Change Management

### How to Request Changes
1. Create an issue describing the change
2. Discuss with team
3. Get approval from PM Agent or owner
4. Implement change
5. Test thoroughly
6. Merge to main

### Impact Assessment
- Does it affect database schema?
- Does it affect API contracts?
- Does it affect UI/UX?
- Does it affect permissions/security?
- Does it affect existing features?

## 7. Security Standards

### Authentication
- Use JWT for API authentication
- Set appropriate token expiration (24h)
- Validate tokens on every protected endpoint

### Authorization
- Check user role before allowing admin actions
- Validate ownership before allowing task updates
- Never trust client-side role checks alone

### Input Validation
- Validate all user inputs on backend
- Sanitize inputs to prevent XSS
- Use parameterized queries to prevent injection
- Validate file uploads (type, size)

### Password Security
- Hash passwords with bcrypt (salt rounds: 10)
- Never store plain text passwords
- Enforce minimum password requirements

## 8. Performance Standards

### Frontend
- Initial load time: < 3 seconds
- Optimize images (compress, lazy load)
- Minify CSS/JS in production

### Backend
- API response time: < 500ms
- Database queries: < 100ms
- Use indexes for frequently queried fields

## 9. Deployment Standards

### Pre-deployment Checklist
- [ ] All tests passed
- [ ] No console errors
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Backup created

### Deployment Process
1. Deploy backend
2. Run database migrations if needed
3. Deploy frontend
4. Smoke test
5. Monitor for errors
