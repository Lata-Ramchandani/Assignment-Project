from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import time, threading


class AssignmentModel(models.Model):
    name=models.CharField(max_length=150)


@receiver(post_save, sender=AssignmentModel)
def assignment_handler(sender, instance, **kwargs):
    # By default, Django signals are executed synchronusly
    # Yes, Django signals run in the same thread as the caller
    # As caller and the signal handler have same thread ID
    # Yes, by default Django signals run in the same database transaction as the caller

    print(f"Signal Received in thread:{threading.get_ident()}")
    print("Wait for 3 seconds")
    time.sleep(3)
    print(f"Signal Processed for object: {instance.name}")
