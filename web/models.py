from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"Contact Form from {self.customer_name} ({self.customer_email})"

class Comentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE, related_name='comentaries')
    txt = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.txt[:20]}"