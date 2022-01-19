
from controllers.input_validation import *
from models.template import *

add_player_questions = [
    Interface("input", "first_name", "Entrer le prénom du joueur:",validator=StringValidator).menu(),
    Interface("input", "last_name", "Entrer le nom de famille du joueur: ", validator=StringValidator).menu(),
    Interface(
        "input", "date_of_birth", "Entrer la date de naissance du joueur (JJ/MM/AAAA):", validator=DateValidator
    ).menu(),
    Interface("input", "gender", "Entrer le sexe du joueur (M/F):", validator= GenderValidator).menu(),
    Interface("input", "ranking", "Entrer le classement du joueur:", validator= PositiveIntegerValidator ).menu(),
]


class Table_display:

    def display_players(data_from_player_table):
        display_table = [['Prénom', 'Nom', 'Naissance', 'Sexe', 'Classement']]
        for player in data_from_player_table:
            display_table.append([player['first_name'][:15], player['last_name'][:15], player['date_of_birth'], player['gender'], player['ranking']])
        t = Texttable()
        t.add_rows(display_table)
        print(t.draw())

    def diplay__and_select_players(data_from_player_table):

        list_player_string = [Separator("{:<18} | {:<16} | {:<10} | {:<5} | {:<10} | {:5}".format("Prénom" , "Nom", "Naissance", "Sexe", "Classment", "ID"))]
        for player in data_from_player_table:
            player_string="{:<16} | {:<16} | {:<10} | {:<5} | {:<10} | {:5}".format(player['first_name'][:15], player['last_name'][:15], player['date_of_birth'], player['gender'], player['ranking'], str(player.doc_id))
            list_player_string.append({'name' : player_string })
        select_player = Interface("checkbox","checked", "Séléctioner les joueurs :", choices= list_player_string).menu()
        selected_player = prompt(select_player)["checked"]
        selected_player_id = []
        for player in selected_player:
            player_id = int(re.split(r"\|",player)[5])
            selected_player_id.append(player_id)
        return selected_player_id
