from django.contrib import admin

from .models import Book, BookStatus, Member

# Register your models here.
admin.site.register(Book)
admin.site.register(BookStatus)
admin.site.register(Member)