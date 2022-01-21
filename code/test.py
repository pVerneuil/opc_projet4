import random 

class Player:
    def __init__(self,id,elo,score=0) :
        self.id = id
        self.score = score
        self.elo = elo
    def set_score(self,result):
        self.score+=result


players_id_sorted = [1,3,4,5,6,7,10,12,30,25,100] #lets assume they are already ranked by ello at this point
number_of_round = 6
number_of_round_played = 0
players_list = []
rounds = {} #rename round
results = {}
# first round
eloo = 3000
for id in players_id_sorted:
    players_list.append(Player(id,eloo))
    eloo-= 10

for i in range(1, number_of_round):
    rounds[f'round{i}'] = []
    results[f'round{i}'] = []
#eventually loop here with sorted player list
if not len(players_list)%2 == 0:
    player_in_this_round = players_list[:-1]
    players_list[len(players_list)-1].set_score(1)
else : player_in_this_round = players_list

#creating matches
i = 0
matches=[]  
for i in range(0, int(len(player_in_this_round)/2)):
    #fix playerA et find player B that valid
    matches.append([player_in_this_round[i],player_in_this_round[len(player_in_this_round)-1-i]])
rounds[f'round{number_of_round_played+1}'] = matches
#check if players already played each other here
#outpout matches
for item in rounds[(f'round{number_of_round_played+1}')]:
    print(f'joueur : {item[0].id} VS joueur : {item[1].id}')

#results
a = []
for matche in rounds[(f'round{number_of_round_played+1}')]:
    r = random.randrange(0, 3, 1)
    a.append([r/2,1-r/2])
results[f'round{number_of_round_played+1}'] = a
print(results)
#set scores
for (result,matche) in zip(results[f'round{number_of_round_played+1}'], rounds[f'round{number_of_round_played+1}']) :
    matche[0].set_score(result[0])
    matche[1].set_score(result[1])
#for player in players_list:
#    print(f'le joueur {player.id} a un score de {player.score}')
#    print(player.elo)

test = sorted(players_list, key=lambda x : (x.score, x.elo ),reverse=True)
#for player in test:
#    print(f'id : {player.id}| score : {player.score} | elo {player.elo}')