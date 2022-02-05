from models.round import Round
from models.player import Player


class Tournament:
    def __init__(
        self,
        name,
        venue,
        starting_date_tournament,
        time_format,
        description,
        number_of_rounds=4,
        number_of_rounds_played=0,
    ):
        self.name = name
        self.venue = venue
        self.starting_date_tournament = starting_date_tournament
        self.time_format = time_format
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.number_of_rounds_played = number_of_rounds_played
        self.players = []
        self.rounds = []

    def serialize(self):
        player_id_list = []
        for player in self.players:
            player_id_list.append(player.id_db)
        round_list = []
        for round in self.rounds:
            round_list.append(round.serialize())

        return {
            "name": self.name,
            "venue": self.venue,
            "starting_date_tournament": self.starting_date_tournament,
            "time_format": self.time_format,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "number_of_rounds_played": self.number_of_rounds_played,
            "players": player_id_list,
            "rounds": round_list,
        }

    def deserialize(tournament_data):
        players = []
        for id in tournament_data["players"]:
            players.append(Player.instantiate_from_db_by_id(id))

        rounds = []
        for round in tournament_data["rounds"]:
            rounds.append(Round.deserialize(round, players))

        this_tournament = Tournament(
            tournament_data["name"],
            tournament_data["venue"],
            tournament_data["starting_date_tournament"],
            tournament_data["time_format"],
            tournament_data["description"],
            tournament_data["number_of_rounds"],
            tournament_data["number_of_rounds_played"],
        )
        this_tournament.players = players
        this_tournament.rounds = rounds
        return this_tournament
