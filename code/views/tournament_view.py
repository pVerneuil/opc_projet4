from controllers.input_validation import *
from models.template import *

create_tournament_questions = [
    Interface("input", "name", "Entrer le Nom du tournois:",validator = StringValidator).menu(),
    Interface("input", "venue", "Entrer le lieu ou se déroule le tournois: ", validator = StringValidator).menu(),
    Interface(
        "input", "starting_date", "Entrer la date de début du tournois (JJ/MM/AAAA):", validator = DateValidator
    ).menu(),
    Interface("input", "time_format", "Entrer le format de contrôle du temps:").menu(),
    Interface("input", "description", "Entrer une rapide description du tournois: ").menu(),
    Interface("input", "number_of_rounds", "Entrer le nombre de ronde", validator = PositiveIntegerValidator ).menu()
]