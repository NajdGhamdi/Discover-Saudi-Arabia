from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
def profile_image_upload(instance,filename):
    txt='imgprofile_'
    imagename,extension=filename.split('.')
    return "profiles/%s%s.%s"%(txt,instance.id,extension)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    image=models.ImageField(upload_to=profile_image_upload)

    def __str__(self):
        return str(self.user)


#SIGNAL IS HAPPEN AFTER WE POST_SAVE THAT'S MEAN AFTER SAVING ANEW USER WE WILL HAVE A NEW PROFILE

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)




