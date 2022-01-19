from models.template import *

main_menu = Interface(
    "list",
    "main_menu_choice",
    "=======  Menu Principal  =======",
    choices=[
        Separator("= Tournois ="),
        "Créer un tournois",
        "Charger un tournois",
        Separator("= Joueurs ="),
        "Ajouté un joueur",
        "Modifier le classement",
        Separator("= Rapports ="),
        "Liste de tout les joueurs",
        "Liste des joueurs d'un tournois",
        "Liste des tounois",
        Separator(),
        "Quitter",
    ],
).menu()
