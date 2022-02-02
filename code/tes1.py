from models.tournament import Tournament
from models.round import Round
from controllers.data_controller import *
from models.player import *


data = DataController.fetch_all_data_from_table(players_table)
tournament = DataController.fetch_all_data_from_table(tournament_table)
""" players = []
for item in tournament[0]['players']:
    players.append(Player.instantiate_from_db_by_id(item))
rounds = []
for round in tournament[0]['rounds']:
    rounds.append(Round.deserialize(round,players))

for round in rounds:
    print (round.name)
    for match in round.matchs :
        print([match[0][0].id_db,match[0][1]],[match[1][0].id_db,match[1][1]])
for player in players :
    print(f'player id :{player.id_db} score : {player.score}') """
print (type(tournament[1]))
#Tournament.deserialize(tournament[1])