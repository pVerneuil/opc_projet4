from models.template import *
from views.player_view import *
from models.player import *


class PlayerController:
    def get_info():
        player_inputs = prompt(add_player_questions,style=style)
        player_inputs['ranking'] = int(player_inputs['ranking'])
        return player_inputs