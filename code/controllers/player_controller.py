from models.player import *
from controllers.data_controller import *


class Player_controller:
    def instantiate_from_db_by_id(id_db):
        """instantiate a player from its database id

        Args:
            id_db (int): id of a player
        """
        player_data = DataController.get_document_by_id(players_table,id_db)
        player =  Player(
            player_data["first_name"],
            player_data["last_name"],
            player_data["date_of_birth"],
            player_data["gender"],
            player_data["ranking"],
            id_db,
        )
        return player

