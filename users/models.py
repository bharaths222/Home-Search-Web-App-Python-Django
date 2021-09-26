from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

# Create a dynamic file path for profile pics by user 
def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.user.id, "profile_pic", filename
      )

# Define Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField(default='0')
    image = models.ImageField(default='default.jpg', blank=True, upload_to=get_upload_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



