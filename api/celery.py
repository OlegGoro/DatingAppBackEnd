from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import task
from celery import shared_task
import django
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from music.models import Claims
from music.models import ChatSession
from music.models import Messages

@app.task(bind=True)
def debug_task(self):
    print ("is works!")
    Claims.objects.all().update(esttime=F('esttime') - 1)
    delete = Claims.objects.all().filter(esttime__lte=0)
    delete.delete()
    ChatSession.objects.all().update(esttime=F('esttime') - 1)
    delete = Messages.objects.filter(chatsession__esttime__lte=0)
    delete.delete()
    delete = ChatSession.objects.filter(esttime__lte=0)
    delete.delete()
