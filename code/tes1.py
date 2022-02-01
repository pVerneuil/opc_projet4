from models.round import Round
from controllers.data_controller import *
from models.player import *

data = DataController.fetch_all_data_from_table(players_table)
tournament = DataController.fetch_all_data_from_table(tournament_table)
player = Player.instantiate_from_db_by_id(4)
# print(player.first_name)
roundys = Round.deserialize(tournament[1]['rounds'])
print(roundys[0].start_datetime)
print(roundys[0].matchs[0][0][0].date_of_birth)
# for roundy in roundys:
#     print (roundy.name)
#     print (roundy.matchs)
