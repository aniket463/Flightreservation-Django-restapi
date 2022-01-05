from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)