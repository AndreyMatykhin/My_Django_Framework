import os

from celery import Celery

import my_braniaclms.settings

if my_braniaclms.settings.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_braniaclms.settings")

celery_app = Celery("braniac")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()