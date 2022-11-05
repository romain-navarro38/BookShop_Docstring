from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def clean_isbn_code(value: str = "") -> str:
    if not value:
        return value

    return "".join([char for char in value.upper() if char.isdigit() or char == "X"])


def validate_isbn10(value: str) -> bool:
    key = value[-1]
    code = [int(char) for char in value[:-1]]
    multiplied = [v1 * v2 for v1, v2 in zip(code, range(10, 1, -1))]
    calculed_key = 11 - sum(multiplied) % 11
    if calculed_key == 11:
        calculed_key = "0"
    elif calculed_key == 10:
        calculed_key = "X"
    else:
        calculed_key = str(calculed_key)
    return key == calculed_key


def validate_isbn13(value: str) -> bool:
    key = value[-1]
    code = [int(char) for char in value[:-1]]
    multiplied = [v1 * v2 for v1, v2 in zip(code, [1, 3] * 6)]
    calculed_key = str(10 - sum(multiplied) % 10)
    if calculed_key == "10":
        calculed_key = "0"
    return key == calculed_key and value[:3] in ("978", "979")


def validate_isbn(value: str):
    cleaned_value = clean_isbn_code(value)
    if not cleaned_value[:-1].isdigit():
        return False

    if len(cleaned_value) == 10 and not validate_isbn10(cleaned_value):
        raise ValidationError(
            _('%(value)s is not an ISBN valide'),
            params={'value': value},
        )
    if len(cleaned_value) == 13 and not validate_isbn13(cleaned_value):
        raise ValidationError(
            _('%(value)s is not an ISBN valide'),
            params={'value': value},
        )
