import random 
import copy
from test1 import *
import snoop

class Player:
    def __init__(self,id,elo,score=0) :
        self.id = id
        self.score = score
        self.elo = elo
    def set_score(self,result):
        self.score+=result

class Round:
    def __init__(self, name, starting_time) -> None:
        self.starting_time = starting_time
        self.name = name
        self.matchs = []
    def register_match(self, joueur1 : object, joueur2 : object):
        match = tuple(([joueur1, 0],[joueur2, 0]))
        self.matchs.append(match)
        



players_id_sorted = [1,3,4,5,6,7,10,12,30,25] #lets assume they are already ranked by elo at this point
number_of_round = 6
number_of_round_played = 0
players_in_the_tournament= [] 
tournament_rounds = []

#set up delet later

elo = 3000

for id in players_id_sorted:
    players_in_the_tournament.append(Player(id,elo))
    elo-= 10
#!first round

#even thing only append the first time I think

if not is_even(len(players_in_the_tournament)):
    players_in_this_round = copy.copy(players_in_the_tournament)
    players_in_the_tournament.pop().set_score(1)
else : 
    players_in_this_round  = copy.copy(players_in_the_tournament)
#eventually loop here with sorted player list



tournament_rounds.append(Round('round1',"15H30 11/10/2022"))
for i in range(0, int(len(players_in_this_round)/2)):
    tournament_rounds[0].register_match(players_in_this_round[i], players_in_this_round[len(players_in_this_round)-1-i])

#outpout matches
current_round = f'round{number_of_round_played+1}'

for match in tournament_rounds[0].matchs:
    print(f'joueur : {match[0][0].id} VS joueur : {match[1][0].id}')
#random results and set score
for match in tournament_rounds[number_of_round_played].matchs:
    r = random.randrange(0, 3, 1)
    match[0][1] = r/2
    match[0][0].set_score(r/2)
    match[1][1] = 1-r/2
    match[1][0].set_score(1-r/2)
    
#display results
for player in players_in_the_tournament:
    print(f'le joueur {player.id} a un score de {player.score}')
    print(player.elo)

sorted_test = sorted(players_in_the_tournament, key = lambda x : (x.score, x.elo ),reverse=True)
for player in sorted_test:
    print(f'id : {player.id}| score : {player.score} | elo {player.elo}')

@snoop
def check_if_players_met(player1, player2,rounds):
    round_checked = 0
    print(len(tournament_rounds) )
    have_met = False
    while round_checked <len(tournament_rounds):
        for round in rounds:
            for match in round.matchs :
                if match[0][0] == player1:
                    if match[1][0] == player2:
                        have_met = True
                elif match[1][0] == player1:
                    if match[0][0] == player2:
                        have_met = True
        round_checked += 1
    return have_met
'''
'''
l = check_if_players_met(sorted_test[1],sorted_test[0],tournament_rounds)
print(l)


available_players = copy.copy(sorted_test)
def test():
    condition1 = condition(sorted_test,available_players) #! rename condition
    while condition1: #! rename condition
        i= 0
        while not check_if_players_met(available_players[0],available_players[i+1],tournament_rounds): #!round arent the real name
            Round.register_match(available_players.pop(0),available_players.pop(i+1),tournament_rounds)#! same here
            i+=1
            if i > len(available_players):
                Round.register_match(available_players.pop(0),available_players.pop(1),tournament_rounds)
                break
        condition1 = condition(sorted_test,available_players) #! rename condition
test()
"""
"""