from .base import *

DEBUG = True
ALLOW_ROBOTS = True

if DEBUG_TOOLBAR:
    INTERNAL_IPS = ["127.0.0.1"]

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
