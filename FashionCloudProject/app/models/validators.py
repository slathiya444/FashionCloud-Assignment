from django.core.exceptions import ValidationError
import re


def validate_alphanumeric(value):
    if not value.isalnum():
        raise ValidationError("Value must contain only alphanumeric characters.")


def validate_article(value):
    regex = r'\d{5,7}-\d{2,5}$'  # Regular expression pattern
    if not re.match(regex, value):
        raise ValidationError('Code must be in the format XXXX-XX (digits-hyphen-digits).')

