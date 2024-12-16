from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.TextField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="recipieImg")

    def __str__(self):
        return f"{self.title}"