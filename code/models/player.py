from controllers.data_controller import *
class Player:
    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        gender,
        ranking,
        id
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.id = id
    
    def add_player_db(data_player):
        DataController.add_one_to_db(table=players_table,data=data_player)

