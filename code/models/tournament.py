class Tournament:
    def __init__(
        self,
        name,
        venue,
        starting_date,
        rounds,
        time_format,
        description,
        max_player,
        number_of_rounds=4,
    ):
        self.name = name
        self.venue = venue
        self.starting_date = starting_date
        self.rounds = rounds
        self.time_format = time_format
        self.descrition = description
        self.max_players = max_player
        self.players = []
        self.number_of_rounds = number_of_rounds

    def add_player(self, player):
        if len(self.players) < self.max_players :
            self.players.append(player)
            return True
        return False
