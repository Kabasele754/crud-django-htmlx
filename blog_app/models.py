from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-create"]

    def image_tag(self):  # new
        return mark_safe(f'<img  src="/../../media/{self.image}" width="150" height="100" />')

