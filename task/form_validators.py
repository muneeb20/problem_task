from django.core.validators import RegexValidator
from task.models import CustomUser


class FormValidators(object):
    CHAR_VALIDATOR = RegexValidator(r'^[a-zA-Z\s]*$', 'Only characters are allowed.')
