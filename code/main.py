from views.menus_view import main_menu
from views.player_view import *
from views.tournament_view import *
from models.player import *
from controllers.tournament_controller import *


while True:
    all_players_data = DataController.fetch_all_data_from_table(players_table)
    all_tournaments_data = DataController.fetch_all_data_from_table(tournament_table)
    main_menu_choice = prompt(main_menu, style=style)

    # creating and playing a tournament
    if main_menu_choice["main_menu_choice"] == "Créer un tournois":
        tournament_inputs = prompt(create_tournament_questions, style=style)
        players_id_selected = TableDisplay.display_and_select_players(
            all_players_data, 8, "Veuillez selectioner 8 joueurs minimun."
        )
        if Interface.confirm(
            "Confirmer la création du tournois et commencer celui ci? (O/N)"
        ):
            this_tournament = TournamentController.instanciate_from_user_inputs(
                players_id_selected, tournament_inputs
            )
            this_tournament_id = DataController.add_one_to_db(
                Tournament.serialize(this_tournament), tournament_table
            )
            print("Tournois créé")
            TournamentController.play_tournament(this_tournament, this_tournament_id)
        else:
            print("Retour au Menu Principal")

    # Loading and playing a tournament
    if main_menu_choice["main_menu_choice"] == "Charger un tournois":
        TournamentController.load_and_play_tournament()

    # add a player to the database
    if main_menu_choice["main_menu_choice"] == "Ajouté un joueur":
        player_inputs = PlayerView.get_info()
        if Interface.confirm("Confirmer l'enregistrement du joueur? (O/N)"):
            Player.add_player_db(player_inputs)
            print("Joueur Ajouté")
        else:
            print("Retour au Menu Principal")
    # modify the elo of players
    if main_menu_choice["main_menu_choice"] == "Modifier le classement elo des joueurs":
        PlayerView.update_elo_ranking(all_players_data)

    # display repports
    if main_menu_choice["main_menu_choice"] == "Liste de tout les joueurs":
        PlayerView.player_report(all_players_data)

    if main_menu_choice["main_menu_choice"] == "Liste des tounois":
        TournamentView.display_tournaments(all_tournaments_data, "Tournois enregistés")
    if main_menu_choice["main_menu_choice"] == "Liste des joueurs d'un tournois":
        TournamentView.report_players_in_tournament()

    if (
        main_menu_choice["main_menu_choice"]
        == "Liste des Rondes et Matchs d'un tournois"
    ):
        id_selected_tournament = TournamentView.display_and_select_tournament(
            all_tournaments_data,
            "=== Tournois ===",
            "Selectionez l'id d'un tournois pour en afficher les joueurs:",
        )
        RoundView.report_rounds_and_matchs(
            DataController.get_document_by_id(tournament_table, id_selected_tournament)
        )
    # quit the program
    if main_menu_choice["main_menu_choice"] == "Quitter":
        break
