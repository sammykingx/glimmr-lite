APP_CSP_POLICY = {
    'default-src': ["'self'"],
    'script-src': [
        "'self'",
    ],
    'style-src': [
        "'self'",
    ],
    'font-src': ["https://fonts.gstatic.com"],
    'img-src': ["'self'", 'data:'],
    'connect-src': ["'self'",], # Allow connections to the same origin
    'frame-ancestors': ["'none'"],  # Prevent clickjacking
    # 'object-src': ["'none'"],  # Prevent loading plugins
    # 'base-uri': ["'self'"],  # Restrict base URI to the same origin
    # 'form-action': ["'self'"],  # Restrict form submission to the same origin
    # 'upgrade-insecure-requests': True,  # Upgrade HTTP requests to HTTPS
    # 'block-all-mixed-content': True,  # Block mixed content
}
