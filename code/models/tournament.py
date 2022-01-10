class Tournament:
    def __init__(
        self,
        name,
        venue,
        starting_date,
        rounds,
        time_format,
        description,
        number_of_rounds=4,
    ):
        self.name = name
        self.venue = venue
        self.starting_date = starting_date
        self.rounds = rounds
        self.time_format = time_format
        self.descrition = description
        self.number_of_rounds = number_of_rounds
        self.players = []

    def create_round(self): #a mettre dans le controler
        pass
