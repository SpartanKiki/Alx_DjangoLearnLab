# Advanced Features and Security – Django

This project demonstrates advanced Django features with a focus on security, authentication, and authorization.

## Features Implemented

- Custom Django app `bookshelf`
- Book model with custom permissions
- Role-based access control using Groups:
  - Viewers: Read-only access
  - Editors: Can add and edit books
  - Admins: Full control
- Permission enforcement using decorators in views
- Django Admin configuration
- Secure access handling with permission checks

## Key Concepts Covered

- Django permissions and groups
- `@permission_required` decorator
- Secure view access with `raise_exception=True`
- Admin-based role management

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations
5. Start the development server

```bash
python manage.py migrate
python manage.py runserver

## HTTPS & Security Review

This project enforces HTTPS and secure communication using Django's
recommended security settings.

### Implemented Measures:
- Automatic redirection from HTTP to HTTPS
- HTTP Strict Transport Security (HSTS)
- Secure session and CSRF cookies
- Protection against clickjacking (X-Frame-Options)
- Protection against MIME sniffing
- Browser XSS filtering enabled

### Benefit:
These configurations protect user data in transit and reduce the risk
of common web attacks such as XSS, CSRF, and clickjacking.
