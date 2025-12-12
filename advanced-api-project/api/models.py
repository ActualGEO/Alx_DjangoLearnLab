from django.db import models

# Create your models here.
class Author(models.Model):
    #This creates a author model
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    """The book map every object of book model to
       a specific author
    """

    title = models.CharField(max_length=150)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

