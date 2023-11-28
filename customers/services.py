from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django.core.validators import RegexValidator


def validate_phone_number(value):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Номер телефона должен быть в формате: '+999999999'.",
    )
    phone_regex(value)
