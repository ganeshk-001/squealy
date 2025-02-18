from celery.task.schedules import crontab
from celery.decorators import periodic_task

from email_service import send_emails

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def trigger_emails():
    send_emails()
