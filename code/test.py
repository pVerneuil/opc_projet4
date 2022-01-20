from mimetypes import init
from nis import match
from unittest import result
import random 

class Player:
    def __init__(self,id,score=0) :
        self.id = id
        self.score = score
    def set_score(self,result):
        self.score+=result


players_id_sorted = [1,3,4,5,6,7,10,12,30,25,100] #lets assume they are already ranked by ello at this point
number_of_round = 6
number_of_round_played = 0
players_list = []
matches = {} #rename round
results = {}
# first round
for id in players_id_sorted:
    players_list.append(Player(id))
#eventually loop here with sorted player list
if not len(players_list)%2 == 0:
    player_in_this_round = players_list[:-1]
    players_list[len(players_list)-1].set_score(1)
else : player_in_this_round = players_list

#creating matches
i = 0
temp=[] #matches 
for i in range(0, int(len(player_in_this_round)/2)):
    #fix playerA et find player B that valid
    temp.append([player_in_this_round[i],player_in_this_round[len(player_in_this_round)-1-i]])
matches[f'round{number_of_round_played+1}'] = temp
#check if players already played each other here
#outpout matches
for item in matches[(f'round{number_of_round_played+1}')]:
    print(f'joueur : {item[0].id} VS joueur : {item[1].id}')

#results
a = []
for matche in matches[(f'round{number_of_round_played+1}')]:
    r = random.randrange(0, 3, 1)
    a.append([r/2,1-r/2])
results[f'round{number_of_round_played+1}'] = a
print (results)

#set scores
