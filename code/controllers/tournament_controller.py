from models.tournament import Tournament
from models.player import Player
from models.round import Round
from controllers.round_controller import Round_controller
from controllers.data_controller import DataController, tournament_table
from views.round_view import RoundView
from views.player_view import TableDisplay
from views.tournament_view import TournamentView
from tinydb.operations import add


class TournamentController:
    def instanciate_from_user_inputs(player_id_selected, tournament_inputs):
        this_tournament = Tournament(
            tournament_inputs["name"],
            tournament_inputs["venue"],
            tournament_inputs["starting_date_tournament"],
            tournament_inputs["time_format"],
            tournament_inputs["description"],
            number_of_rounds=int(tournament_inputs["number_of_rounds"]),
        )
        for id in player_id_selected:
            this_tournament.players.append(Player.instantiate_from_db_by_id(id))
        return this_tournament

    def play_tournament(tournament: object, tournament_id):
        while tournament.number_of_rounds_played < tournament.number_of_rounds:
            # instanciate the round
            this_round = Round(f"round{tournament.number_of_rounds_played+1}")
            tournament.rounds.append(this_round)
            this_round.set_date_and_time(True)

            # creating matchs for the round and displaying it
            if tournament.number_of_rounds_played == 0:
                Round_controller.create_matchs_for_first_round(
                    tournament.players, this_round
                )
            if tournament.number_of_rounds_played > 0:
                Round_controller.create_matchs_for_this_round(
                    tournament.players,
                    tournament.rounds[tournament.number_of_rounds_played],
                    tournament.rounds,
                )
            RoundView.display_matchs_in_this_round(this_round)
            # get the results inputs
            RoundView.get_and_registrer_matchs_result(this_round)
            this_round.set_date_and_time(False)
            tournament.number_of_rounds_played += 1

            # display the results
            Round_controller.sort_player_list_by_score_then_elo(tournament.players)
            if tournament.number_of_rounds_played == tournament.number_of_rounds:
                TableDisplay.display_players_score(
                    "Classement Final", tournament.players
                )
            else:
                TableDisplay.display_players_score(
                    f"Classement Ronde {tournament.number_of_rounds_played}",
                    tournament.players,
                )
            # updating the database
            DataController.update_by_id(
                tournament_table,
                {"number_of_rounds_played": tournament.number_of_rounds_played},
                tournament_id,
            )
            tournament_table.update(
                add("rounds", [this_round.serialize()]), doc_ids=[tournament_id]
            )

    def return_unfinished_tournaments():
        unfinished_tournaments = []
        for tournament in DataController.fetch_all_data_from_table(tournament_table):
            if tournament["number_of_rounds"] > tournament["number_of_rounds_played"]:
                unfinished_tournaments.append(tournament)
        return unfinished_tournaments

    def load_and_play_tournament():
        selected_tournament = TournamentView.display_and_select_tournament(
            TournamentController.return_unfinished_tournaments(),
            "Tournois non terminé(s)",
            "Veuiller selectioner l'id d'un tournois à charger :",
            True,
        )
        TournamentController.play_tournament(
            Tournament.deserialize(
                DataController.get_document_by_id(tournament_table, selected_tournament)
            ),
            selected_tournament,
        )
