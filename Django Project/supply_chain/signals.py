from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Council, Project, Department

@receiver(post_save, sender=Council)
def notify_council_creation(sender, instance, created, **kwargs):
    if created:
            subject='New Council Created'
            message=f'A new council named "{instance.name}" has been created.'

            send_mail(
                subject,
                message,
                None,
                ['admin@example.com'],
                fail_silently=False,
            )