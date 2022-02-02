from views.player_view import *
from controllers.data_controller import *
from views.round_view import RoundView
from models.round import Round
from models.tournament import Tournament
from models.player import Player
from controllers.round_controller import Round_controller
from tinydb.operations import add


class TournamentController:
    def save_tournament():
        pass

    def instanciate_from_user_inputs(player_id_selected, tournament_inputs):
        this_tournament = Tournament(
            tournament_inputs["name"],
            tournament_inputs["venue"],
            tournament_inputs["starting_date_tournament"],
            tournament_inputs["time_format"],
            tournament_inputs["description"],
            number_of_rounds=int(tournament_inputs["number_of_rounds"])
        )
        for id in player_id_selected:
            this_tournament.players.append(
                Player.instantiate_from_db_by_id(id)
            )
        return this_tournament
    
    def play_tournament(tournament : object, tournament_id):
        if tournament.number_of_rounds_played == 0:

            round1 = Round('round1')
            tournament.rounds.append(round1)
            round1.set_date_and_time(True)

            Round_controller.create_matches_for_first_round(tournament.players,round1)
            RoundView.display_matches_in_this_round(round1)

            RoundView.get_and_registrer_matchs_result(round1)
            round1.set_date_and_time(False)
            tournament.number_of_rounds_played = 1

            Round_controller.sort_player_list_by_score_then_elo(tournament.players)
            TableDisplay.display_players_score("Classement Ronde 1", tournament.players)

            DataController.update_by_id(
                tournament_table ,
                {'number_of_rounds_played': tournament.number_of_rounds_played},
                tournament_id)
            DataController.update_by_id(
                tournament_table ,
                {'rounds': [round1.serialize()] },
                tournament_id)
            
        while tournament.number_of_rounds_played > 0 and tournament.number_of_rounds_played < tournament.number_of_rounds :

            this_round = Round(f'round{tournament.number_of_rounds_played+1}')
            tournament.rounds.append(this_round)
            this_round.set_date_and_time(True)

            Round_controller.create_matches_for_this_round(
                tournament.players,
                tournament.rounds[tournament.number_of_rounds_played],
                tournament.rounds)
            RoundView.display_matches_in_this_round(this_round)

            RoundView.get_and_registrer_matchs_result(this_round)
            this_round.set_date_and_time(False)
            tournament.number_of_rounds_played += 1

            Round_controller.sort_player_list_by_score_then_elo(tournament.players)
            if tournament.number_of_rounds_played == tournament.number_of_rounds :
                TableDisplay.display_players_score(f"Classement Final", tournament.players)
            else:
                TableDisplay.display_players_score(f"Classement Ronde {tournament.number_of_rounds_played}", tournament.players)
            DataController.update_by_id(
                tournament_table ,
                {'number_of_rounds_played': tournament.number_of_rounds_played},
                tournament_id)
            tournament_table.update(add('rounds', [this_round.serialize()]) ,doc_ids = [tournament_id])