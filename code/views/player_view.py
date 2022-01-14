from PyInquirer import prompt, Separator, Token, style_from_dict
from prompt_toolkit.validation import Validator, ValidationError
import re
from controllers.input_validation import StringValidator
from models.template import *
#TODO validatooor
add_player_questions = [
    Interface("input", "first_name", "Entrer le prénom du joueur:",validator=StringValidator).menu(),
    Interface("input", "last_name", "Entrer le nom de famille du joueur: ", validator=StringValidator).menu(),
    Interface(
        "input", "date_of_birth", "Entrer la date de naissance du joueur (JJ/MM/AAAA):"
    ).menu(),
    Interface("input", "gender", "Entrer le sexe du joueur (M/F):").menu(),
    Interface("input", "ranking", "Entrer le classement du joueur:").menu(),
]