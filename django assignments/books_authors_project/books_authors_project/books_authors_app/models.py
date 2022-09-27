from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors = ... 



class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    notes = models.TextField(null = True)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(null = True)
