from django.conf import settings
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

def user_directory_path(instance, file):
    # file will be saved to user seperated folders
    return 'logos/agent_{}/{}'.format(instance.user.id, file)


class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='agent', on_delete=models.CASCADE,
        primary_key=True)
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55)
    is_company = models.BooleanField(default=False)
    is_independent = models.BooleanField(default=False)
    about = models.TextField()
    phonenumber = PhoneNumberField(blank=True)
    line_id = models.CharField(max_length=25, unique=True, blank=True)
    logo = models.ImageField(upload_to=user_directory_path, default='logos/default.jpeg')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContentManager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    primary_key=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    bio = models.TextField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class VerificicationDocument(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='document', on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    document = models.FileField(upload_to='documents')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name


