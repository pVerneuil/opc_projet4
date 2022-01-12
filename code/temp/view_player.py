from PyInquirer import prompt, Separator, Token, style_from_dict
from prompt_toolkit.validation import Validator, ValidationError
import re
from model_view import *

add_player_questions = [
    Interface("input", "first_name", "Entrer le prénom du joueur:").menu(),
    Interface("input", "last_name", "Entrer le nom de famille du joueur: ").menu(),
    Interface(
        "input", "date_of_birth", "Entrer la date de naissance du joueur (JJ/MM/AAAA):"
    ).menu(),
    Interface("input", "gender", "Entrer le sexe du joueur (M/F):").menu(),
    Interface("input", "ranking", "Entrer le classement du joueur:").menu(),
]
print(add_player_questions)
#prompt(add_player_questions,style= style)