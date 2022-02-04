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
        "Modifier le classement elo des joueurs",
        Separator("= Rapports ="),
        "Liste de tout les joueurs",
        "Liste des tounois",
        "Liste des joueurs d'un tournois",
        "Liste des Rondes et Matchs d'un tournois",
        Separator(),
        "Quitter",
    ],
).menu()
