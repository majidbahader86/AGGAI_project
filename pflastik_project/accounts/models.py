from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_farmer = models.BooleanField(default=False)
    is_scientist = models.BooleanField(default=False)
    # is_user = models.BooleanField(default=False)
    
class Foo(models.Model):
    USER_CHOICES = (
        ('S', 'Scientist'),
        ('F', 'Farmer'),
    )
    user = models.CharField(max_length=1, choices=USER_CHOICES)

    def __str__(self):
        return dict(self.USER_CHOICES).get(self.user, 'Unknown')

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

