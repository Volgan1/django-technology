DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "techno_db",
        "USER": "djangoproject",
        "PASSWORD": "IuLptJ7XEilfxp7joukV",
    }
}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
INSTALLED_APPS += (
"debug_toolbar",
)
