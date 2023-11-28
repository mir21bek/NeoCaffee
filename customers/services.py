from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_phone_number(value):
    phone_regex = RegexValidator(
        regex="^\+?1?\d{9,15}$",
        message="Номер телефона должен быть в формате: '+999999999'.",
    )
    try:
        phone_regex(value)
    except ValidationError:
        raise ValidationError("Invalid phone number format")
