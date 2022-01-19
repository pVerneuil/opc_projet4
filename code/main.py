from views.menus_view import *
from views.player_view import *
from views.tournament_view import *
from models.player import *
from controllers.player_controller import *
        
while True:
    all_player_data = DataController.fetch_all_data_from_table(players_table)
    main_menu_choice = prompt(main_menu, style=style)

    if main_menu_choice["main_menu_choice"] == "Créer un tournois":
        tournament_inputs = prompt(create_tournament_questions,style=style)
        if Interface.confirm("Confirmer la création du tournois? "):
            print('Tournois créer')
        else: print('Retour au Menu Principal')

    if main_menu_choice["main_menu_choice"] == "Ajouté un joueur":
        player_inputs = PlayerController.get_info()
        if Interface.confirm("Confirmer l'enregistrement du joueur? "):
            Player.add_player_db(player_inputs)
            print('Joueur Ajouté')
        else: print('Retour au Menu Principal')
    
    if main_menu_choice["main_menu_choice"] == "Liste de tout les joueurs":
        while True:
            Table_display.display_players(all_player_data)
            if Interface.confirm("Retouner au menu principal?"):
                break

    if main_menu_choice["main_menu_choice"] == "Quitter":
        break
    