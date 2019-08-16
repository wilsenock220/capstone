from django.conf import settings
from django.urls import reverse
from django.db import models

def user_directory_path(instance, file):
    return 'blog/user_{}/{}'.format(instance, file)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    slug = models.SlugField()
    subtitle = models.CharField(max_length=122, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to=user_directory_path)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug,})
    

