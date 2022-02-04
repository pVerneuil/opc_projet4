from models.template import *
from controllers.data_controller import *
from rich.console import Console
from rich.table import Table
class RoundView:
    def display_matches_in_this_round(round):
        print(f'=== Matchs du {round.name} ===')
        for match in round.matchs:
            print(
                f"{match[0][0].first_name} {match[0][0].last_name} contre {match[1][0].first_name} {match[1][0].last_name}"
            )

    def get_and_registrer_matchs_result(round):
        i = 1
        for match in round.matchs:
            inputs_result = prompt(Interface(
                "list",
                "result",
                f"Gagnant du match {i}",
                choices=[
                    f"{match[0][0].first_name} {match[0][0].last_name}",
                    f"{match[1][0].first_name} {match[1][0].last_name}",
                    "Match Nul"
                ]
            ).menu(), style=style)
            if inputs_result['result'] == "Match Nul":
                match[0][0].set_score(0.5)
                match[0][1] = 0.5
                match[1][0].set_score(0.5)
                match[1][1] = 0.5
            if inputs_result['result'] == f"{match[0][0].first_name} {match[0][0].last_name}":
                match[0][0].set_score(1)
                match[0][1] = 1
            if inputs_result['result'] == f"{match[1][0].first_name} {match[1][0].last_name}":
                match[1][0].set_score(1)
                match[1][1] = 1
            i += 1

    def report_rounds_and_matchs(tournament):
        players_dict ={}
        for id in tournament["players"]:
            player_data = DataController.get_document_by_id(players_table,id)
            players_dict[f'{id}'] =(f"{player_data['first_name']} {player_data['last_name']}")
        rounds = Table(title=f"=== Rapport du tournois {tournament['name']} ===")
        rounds.add_column("Nom", justify="left", style="magenta")
        rounds.add_column("Début", justify="right", style="cyan")
        rounds.add_column('Fin', justify="right", style="cyan")
        rounds.add_column('Matchs', justify='center', style='green')
        for round in tournament['rounds']:
            matchs = Table(title="",show_lines=True,collapse_padding=True)
            matchs.add_column("Joueur 1", justify="left", style="magenta")  
            matchs.add_column("Joueur 2", justify="left", style="magenta")
            matchs.add_column("Vainqueur", justify="left", style="green") 
            for match in round["matchs"]:
                if match[0][1] == 1:
                    winner = players_dict[f"{match[0][0]}"]
                if match[0][1] == 0:
                    winner = players_dict[f"{match[1][0]}"]
                if match[0][1] == 0.5:
                    winner = "Match Nul"
                matchs.add_row(players_dict[f"{match[0][0]}"], players_dict[f"{match[1][0]}"], winner)
            
            rounds.add_row(round['name'], round['start_datetime'], round['end_datetime'], matchs)
        console = Console()
        console.print(rounds)