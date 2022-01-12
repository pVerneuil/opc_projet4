from view_menus import *
from view_player import *

a = prompt(main_menu, style=style)
print(a)

if a["main_menu_choice"] == "Ajouté un joueur":
    b = prompt(add_player_questions,style=style)
