from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    isbn_num = models.CharField(max_length=150)
    genre = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.title

class BookStatus(models.Model):
    STATUSES = (
        ("Issued", "issued"),
        ("Available", "available"),
        ("Unavailable", "unavailable")
    )
    status = models.CharField(max_length=100, choices=STATUSES)
    member = models.ForeignKey(
        "Member",
        on_delete=models.CASCADE,
        related_name="user_status",
        blank=True,
        null=True
    )
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="book_status"
    )
    created_on = models.DateTimeField(auto_now_add=True)
