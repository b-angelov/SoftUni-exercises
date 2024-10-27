from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,
        validators=(MinLengthValidator(5),),
        error_messages={
            "unique": "Oops! That title is already taken. How about something fresh and fun?",
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        help_text="Share your funniest furry photo URL!"
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now=True,
        editable=False,
    )

    author = models.ForeignKey(
        to='authors.Author',
        on_delete=models.CASCADE, # May have been modified afterward, beware the requirements!
        editable=False,
    )