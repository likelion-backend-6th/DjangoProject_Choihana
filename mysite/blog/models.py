from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF',' Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique = True, help_text='one word for title alias')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['publish']),

        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',args=(self.pk,))

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"comment by {self.name} on {self.post}"
