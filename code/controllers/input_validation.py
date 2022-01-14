import re
from prompt_toolkit.validation import Validator, ValidationError

class StringValidator(Validator):
    def validate(self, document):
        ok = re.match('^[A-Za-z]{3,}$', document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez a n\'utiliser que des lettres (minimun 3)',
                cursor_position=len(document.text))  # Move cursor to end