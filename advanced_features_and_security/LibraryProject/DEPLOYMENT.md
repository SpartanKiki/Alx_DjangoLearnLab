# HTTPS Deployment Configuration

This Django application is configured to enforce HTTPS connections
using Django's built-in security settings.

## SSL/TLS Setup (Production)

In a production environment, HTTPS should be enabled using a web server
such as Nginx or Apache.

### Example (Nginx):
- Obtain an SSL certificate (e.g., via Let's Encrypt)
- Configure the server to listen on port 443
- Redirect all HTTP (port 80) traffic to HTTPS

### Key Django Settings Used:
- SECURE_SSL_REDIRECT = True
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True

These settings ensure that all traffic and cookies are transmitted securely.
