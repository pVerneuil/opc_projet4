from controllers.data_controller import DataController
from controllers.data_controller import players_table


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

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.elo,
        }

    def instantiate_from_db_by_id(id_db):
        """instantiate a player from its database id

        Args:
            id_db (int): id of a player
        """
        player_data = DataController.get_document_by_id(players_table, id_db)
        return Player.deserialize(player_data, id_db)

    def deserialize(player_data, id_db):
        player = Player(
            player_data["first_name"],
            player_data["last_name"],
            player_data["date_of_birth"],
            player_data["gender"],
            player_data["ranking"],
            id_db,
        )
        return player
