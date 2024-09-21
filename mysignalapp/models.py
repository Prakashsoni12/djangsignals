from django.db import models
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time
# Create your models here.



# Model for testing signals
class MyModel(models.Model):
    name = models.CharField(max_length=100)


# Log model to track signal actions
class SignalLog(models.Model):
    message = models.CharField(max_length=100)


# Signal receiver to demonstrate synchronous execution, thread context, and transaction management
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal receiver started...")
    
    # 1. Demonstrating that signals are synchronous
    print("Signal running synchronously - executing a delay for 5 seconds")
    time.sleep(5)
    
    # 2. Demonstrating same-thread execution
    print(f"Signal is running in thread ID: {threading.get_ident()}")

    # 3. Demonstrating signals running within the same transaction
    SignalLog.objects.create(message="Signal was triggered inside transaction.")
    print("Signal receiver completed.")


