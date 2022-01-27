from controllers.data_controller import *


class Player:
    def __init__(
        self, first_name, last_name, date_of_birth, gender, elo, id_db, score=0
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo
        self.id_db = id_db
        self.score = score

    def add_player_db(data_player):
        DataController.add_one_to_db(table=players_table, data=data_player)

    def set_score(self, result):
        self.score += result
