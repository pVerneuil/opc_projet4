from models.tournament import Tournament
from controllers.player_controller import Player_controller


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
            number_of_rounds=tournament_inputs["number_of_rounds"],
        )
        for id in player_id_selected:
            this_tournament.players.append(
                Player_controller.instantiate_from_db_by_id(id)
            )
        return this_tournament
