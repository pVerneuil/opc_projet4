from views.menus_view import *
from views.player_view import *
from models.player import *

a = prompt(main_menu, style=style)
if a["main_menu_choice"] == "Ajouté un joueur":
    b = prompt(add_player_questions,style=style)
print('validation (Y/N) goes here')

Player.add_player_db(b)