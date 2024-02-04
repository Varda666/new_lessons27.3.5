from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

from users.models import User


@shared_task
def _send_mail_email(recipient_list):
    send_mail(
        subject='Обновление курса',
        message=f'Курс, на который вы подписаны, обновлен.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_list]
    )


@shared_task
def check_last_visit(pk):
    instance = User.objects.filter(pk=pk).first
    days_after_last_visit = datetime.date.today() - instance.last_visit
    if days_after_last_visit > 30:
        return False
    return True





