from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(
                'Ensure this value contains only letters.'
            )


def below_zero_validator(value):
    if value < 0:
        raise ValidationError(
            'Ensure this value is greater than or equal to 0.'
        )


def max_size_validator(value):
    max_mb = 5
    if value.size > max_mb * 1024 * 1024:
        raise ValidationError(
            'Max file size is 5.00 MB'
        )


class Profile(models.Model):
    MAX_NAME_LENGTH = 15

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(2),
            validate_letters,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(2),
            validate_letters,
        ),
    )

    budget = models.FloatField(
        default=0,
        validators=(
            MinValueValidator(0),
        ),
    )

    profile_image = models.ImageField(

        # !!!
        upload_to='profiles/',

        blank=True, null=True,

        # default is put inside the template
        # default='/static/images/user.png',

        validators=(
            max_size_validator,
        ),
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Expense(models.Model):
    title = models.CharField(
        max_length=30,
    )

    expense_image = models.URLField(
    )

    description = models.TextField(
        blank=True, null=True,
    )

    price = models.FloatField(
    )
