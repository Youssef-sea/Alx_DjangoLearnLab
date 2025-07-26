# Security Measures in advanced_features_and_security Project

This document outlines the key security measures implemented in this Django application.

## 1. Secure Django Settings (`settings.py`)

The following settings have been configured to enhance application security:

-   **`DEBUG = False`**: Disabled in production to prevent exposure of sensitive debugging information.
-   **`ALLOWED_HOSTS`**: Explicitly lists permissible hostnames for the application, preventing HTTP Host header attacks.
-   **`CSRF_COOKIE_SECURE = True`**: Ensures that the CSRF cookie is only sent over HTTPS.
-   **`SESSION_COOKIE_SECURE = True`**: Ensures that the session cookie is only sent over HTTPS.
-   **`SECURE_BROWSER_XSS_FILTER = True`**: Activates the browser's XSS filter, providing an additional layer of defense.
-   **`X_FRAME_OPTIONS = 'DENY'`**: Prevents the application from being embedded in an iframe, mitigating clickjacking attacks.
-   **`SECURE_CONTENT_TYPE_NOSNIFF = True`**: Prevents browsers from MIME-sniffing, ensuring that content is interpreted as intended and reducing XSS risks.
-   **HTTP Strict Transport Security (HSTS)**: (Commented out, but ready for production) `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD` enforce HTTPS for future visits.
-   **SSL Redirect**: (Commented out, but ready for production) `SECURE_SSL_REDIRECT` forces all HTTP traffic to HTTPS.

## 2. CSRF Token Protection (`article_form.html`, `article_confirm_delete.html`)

All HTML forms that accept `POST` requests include `{% csrf_token %}` within the form. This tag generates a hidden input field with a unique token, which Django validates upon form submission. This protects against Cross-Site Request Forgery (CSRF) attacks, ensuring that only requests originating from the trusted domain can submit data.

## 3. Secure Data Access (SQL Injection Prevention in `views.py`)

Data access in views (`blog/views.py`) strictly adheres to Django ORM best practices:

-   **Exclusive use of Django ORM**: All database queries (e.g., `Article.objects.all()`, `get_object_or_404()`, `form.save()`, `article.delete()`) are performed using Django's Object-Relational Mapper. The ORM automatically parameterizes SQL queries, effectively preventing SQL injection vulnerabilities.
-   **Django Forms for Input Validation**: User input from web forms is processed through `ArticleForm` (defined in `blog/forms.py`). Django Forms handle validation, cleaning, and sanitization of data, ensuring that only valid and safe input is processed by the application. Direct manipulation of raw `request.POST` data for database operations is avoided.

## 4. Content Security Policy (CSP)

A Content Security Policy is implemented using `django-csp` middleware and configured in `settings.py`. This policy mitigates Cross-Site Scripting (XSS) attacks by controlling which content sources the browser is allowed to load.

Key directives currently configured in `settings.py`:
-   `CSP_DEFAULT_SRC`: `'self'` (restricts all content to the same origin by default)
-   `CSP_SCRIPT_SRC`: `'self'` (restricts JavaScript to the same origin)
-   `CSP_STYLE_SRC`: `'self'` (restricts CSS to the same origin)
-   `CSP_IMG_SRC`: `'self'`, `'data:'` (restricts images to same origin and allows data URIs)
-   `CSP_FONT_SRC`: `'self'` (restricts fonts to same origin)
-   `CSP_CONNECT_SRC`: `'self'` (restricts network connections to same origin)

**Note:** The CSP configuration is a starting point and may need to be expanded based on external resources (CDNs, analytics, embedded content) used by the application. `CSP_REPORT_ONLY = True` can be used during development to monitor violations without blocking content.

## 5. Testing Approach

Manual testing has been conducted to verify the implemented security measures:

-   **CSRF Protection**: Attempted to submit forms without the `{% csrf_token %}` (e.g., by manually removing it in browser developer tools), expecting a `403 Forbidden` error.
-   **XSS Prevention**: Tested input fields with `<script>` tags and other malicious JavaScript code to ensure they are rendered as plain text or properly escaped, not executed. Browser console was monitored for CSP violation errors.
-   **SQL Injection**: No direct SQL queries are used, relying on ORM. Any attempt to inject malicious SQL through input fields is handled by Django's ORM and form validation, preventing database manipulation.
-   **Clickjacking**: Tested embedding the application's pages within iframes on external domains, expecting them to be blocked due to `X_FRAME_OPTIONS = 'DENY'` and/or `CSP_FRAME_ANCESTORS`.