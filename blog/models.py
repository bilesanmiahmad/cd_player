from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog_post_detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=100)
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
