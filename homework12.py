from django.db import models
from django.contrib import admin
from models import Book

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "year", "price")
    search_fields = ("title", "author")
    list_filter = ("year",)