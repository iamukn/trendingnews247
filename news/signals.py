# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.management import call_command
from news.models import Posts
import threading

@receiver(post_save, sender=Posts)
def backup_on_new_record(sender, instance, created, **kwargs):
    if created:
        # Run backup in a background thread (so it doesn't block user request)
        threading.Thread(target=run_backup).start()

def run_backup():
    """
    Call Django's 'dbbackup' command or your own custom dump command.
    """
    # call_command('dbbackup')
    ...