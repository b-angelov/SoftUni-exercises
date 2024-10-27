from django.core.validators import MinLengthValidator
from django.db import models

from regular_exam_project_27102024.common.validators import IsAlphaValidator, ExactLengthValidator


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=40,
        validators=(MinLengthValidator(4),IsAlphaValidator(message="Your name must contain letters only!")),
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        validators=(MinLengthValidator(2), IsAlphaValidator(message="Your name must contain letters only!")),
    )

    passcode = models.CharField(
        null=False,
        blank=False,
        validators=(ExactLengthValidator(6,"Your passcode must be exactly 6 digits!"),),
        help_text="Your passcode must be a combination of 6 digits",
    )

    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False
    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return ' '.join((self.first_name,self.last_name))

    @property
    def last_updated_post(self):
        return self.post_set.order_by('-updated_at').first()
