from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title
 

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()

    def __str__(self) -> str:
        return self.content


class Movie(models.Model):
    title = models.CharField(max_length=150)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    plot = models.TextField()
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='movies')

    def __str__(self) -> str:
        return self.title
