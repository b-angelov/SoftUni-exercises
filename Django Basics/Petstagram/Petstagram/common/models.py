from django.db import models

# Create your models here.

class Comment(models.Model):
    comment_text = models.CharField(max_length=300)
    date_and_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey('photos.Photo', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_and_time_of_publication']

class Like(models.Model):
    to_photo = models.ForeignKey('photos.Photo', on_delete=models.CASCADE)
