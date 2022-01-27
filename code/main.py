from views.menus_view import *
from views.player_view import *
from views.tournament_view import *
from models.player import *
from controllers.tournament_controller import *


while True:
    all_player_data = DataController.fetch_all_data_from_table(players_table)
    main_menu_choice = prompt(main_menu, style=style)
    
    if main_menu_choice["main_menu_choice"] == "Créer un tournois":
        tournament_inputs = prompt(create_tournament_questions, style=style)
        players_id_selected = Table_display.display_and_select_players(
            all_player_data
        )  # instancier joueur puis tournois( ou l'invers?)
        if Interface.confirm(
            "Confirmer la création du tournois et commencer celui ci?"
        ):
            this_tournament = TournamentController.instanciate_from_user_inputs(players_id_selected,tournament_inputs)
            print(Tournament.serialize(this_tournament))
            DataController.add_many_to_db(Tournament.serialize(this_tournament),tournament_table)
            print("Tournois créé")

        else:
            print("Retour au Menu Principal")
            
    # comment on what this part do
    if main_menu_choice["main_menu_choice"] == "Ajouté un joueur":
        player_inputs = PlayerView.get_info()
        if Interface.confirm("Confirmer l'enregistrement du joueur? "):
            Player.add_player_db(player_inputs)
            print("Joueur Ajouté")
        else:
            print("Retour au Menu Principal")
            
    # stop
    if main_menu_choice["main_menu_choice"] == "Liste de tout les joueurs":
        while True:
            Table_display.display_players(all_player_data)
            if Interface.confirm("Retouner au menu principal?"):
                break

    if main_menu_choice["main_menu_choice"] == "Quitter":
        break
