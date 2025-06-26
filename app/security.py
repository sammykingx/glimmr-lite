APP_CSP_POLICY = {
    'default-src': ["'self'"],
    'script-src': [
        "'self'",
        "https://cdn.jsdelivr.net",  # Tailwind CDN
        "https://unpkg.com",         # HTMX
    ],
    'style-src': [
        "'self'", 
        #"'unsafe-inline'",  # Required for Tailwind, but unsafe
        "https://fonts.googleapis.com"
    ],
    'font-src': ["https://fonts.gstatic.com"],
    'img-src': ["'self'", 'data:'],
    'connect-src': ["'self'",], # Allow connections to the same origin
    # 'frame-ancestors': ["'none'"],  # Prevent clickjacking
    # 'object-src': ["'none'"],  # Prevent loading plugins
    # 'base-uri': ["'self'"],  # Restrict base URI to the same origin
    # 'form-action': ["'self'"],  # Restrict form submission to the same origin
    # 'upgrade-insecure-requests': True,  # Upgrade HTTP requests to HTTPS
    # 'block-all-mixed-content': True,  # Block mixed content
}
