from celery import task
from celery import shared_task

@task(name='summary')
def send_import_summary():
     print ("fsdfdsf")
