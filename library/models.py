from django.db import models

# Create your models here.

class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('HIS', 'History'),
        ('SCI', 'Science'),
    ]
    title = models.CharField(max_length=50)
    author = models.ManyToManyField('Author')
    publisher = models.CharField(max_length=50)
    publish_date = models.DateTimeField()
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<Author {self.first_name} {self.last_name}>'
