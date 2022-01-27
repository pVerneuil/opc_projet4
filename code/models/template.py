from xmlrpc.client import boolean
from PyInquirer import prompt, Separator, Token, style_from_dict
from controllers.input_validation import YesOrNoValidator
from texttable import Texttable


style = style_from_dict(
    {
        Token.Separator: "#673ab7 bold underline",
        Token.QuestionMark: "#673ab7 bold",
        Token.Selected: "#cc5454",  # default
        Token.Pointer: "#673ab7 bold",
        Token.Instruction: "",  # default
        Token.Answer: "#f44336 bold",
        Token.Question: "",
    }
)


class Interface:
    def __init__(self, type, name, message, choices=None, validator=None):
        self.type = type
        self.name = name
        self.message = message
        self.choices = choices
        self.validator = validator

    def menu(self):
        menu = {"type": self.type, "name": self.name, "message": self.message}
        if self.validator != None:
            menu.update({"validate": self.validator})
        if self.choices != None:
            menu.update({"choices": self.choices})
        return menu

    def confirm(message: str) -> bool:
        menu = {
            "type": "input",
            "message": message,
            "name": "confirm",
            "validate": YesOrNoValidator,
        }
        answer = prompt(menu, style=style)
        result = False
        if answer["confirm"] == "O":
            result = True
        return result
