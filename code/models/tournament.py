from models.round import Round


class Tournament:
    def __init__(
        self,
        name,
        venue,
        starting_date_tournament,
        time_format,
        description,
        number_of_rounds_played=0,
        number_of_rounds=4,
    ):
        self.name = name
        self.venue = venue
        self.starting_date_tounrmanent = starting_date_tournament
        self.time_format = time_format
        self.descrition = description
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
        
        return({
            'name': self.name, 
            'venue': self.venue,
            'starting_date_tounrmanent': self.starting_date_tounrmanent ,
            'time_format': self.time_format ,
            'descrition': self.descrition,
            'number_of_rounds': self.number_of_rounds,
            'number_of_rounds_played': self.number_of_rounds_played,
            'players': player_id_list, 
            'rounds': round_list
            })

    def deserialize(self):
        pass