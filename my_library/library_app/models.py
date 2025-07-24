from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Book title")
    author = models.CharField(max_length=100, help_text="Author name")
    published_date = models.DateField(help_text="Date when book was published")
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True, help_text="International Standard Book Number")
    pages = models.IntegerField(blank=True, null=True, help_text="Number of pages")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Books"