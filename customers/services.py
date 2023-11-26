from django.contrib.auth import models
from django.core.validators import RegexValidator


def validate_phone_number(phone_number):
    phone_regex = RegexValidator(
        regex="^\+?1?\d{9,15}$",
        message="Номер телефона должен быть в формате: '+999999999'.",
    )
    phone_regex(phone_number)
    return phone_number
