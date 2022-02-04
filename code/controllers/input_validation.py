import re
from prompt_toolkit.validation import Validator, ValidationError


class StringValidator(Validator):
    def validate(self, document):
        ok = re.match("^[A-Za-z]{3,}$", document.text)
        if not ok:
            raise ValidationError(
                message="Veuillez à n'utiliser que des lettres (minimun 3)",
                cursor_position=len(document.text),
            )  # Move cursor to end


class PositiveIntegerValidator(Validator):
    def validate(self, document):
        ok = re.match("^[0-9]{1,}$", document.text)
        if not ok:
            raise ValidationError(
                message="Veuillez entrer un entier positif.",
                cursor_position=len(document.text),
            )  # Move cursor to end


class DateValidator(Validator):
    def validate(self, document):
        ok = re.match(
            "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$", document.text
        )
        if not ok:
            raise ValidationError(
                message="Veuillez entrer une date au format (dd/mm/aaaa).",
                cursor_position=len(document.text),
            )  # Move cursor to end


class GenderValidator(Validator):
    def validate(self, document):
        ok = re.match("^[MF]{1}$", document.text)
        if not ok:
            raise ValidationError(
                message="Veuillez entrer M ou F.", cursor_position=len(document.text)
            )  # Move


class YesOrNoValidator(Validator):
    def validate(self, document):
        ok = re.match("^[ON]{1}$", document.text)
        if not ok:
            raise ValidationError(
                message="Veuillez entrer O(oui) ou N(non).",
                cursor_position=len(document.text),
            )
