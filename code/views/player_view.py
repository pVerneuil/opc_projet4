from controllers.input_validation import StringValidator, DateValidator, GenderValidator, PositiveIntegerValidator
from controllers.data_controller import DataController, players_table
from models.template import Interface, style
from rich.console import Console
from rich.table import Table
from PyInquirer import prompt, Separator
import re

add_player_questions = [
    Interface(
        "input", "first_name", "Entrer le prénom du joueur:", validator=StringValidator
    ).menu(),
    Interface(
        "input",
        "last_name",
        "Entrer le nom de famille du joueur: ",
        validator=StringValidator,
    ).menu(),
    Interface(
        "input",
        "date_of_birth",
        "Entrer la date de naissance du joueur (JJ/MM/AAAA):",
        validator=DateValidator,
    ).menu(),
    Interface(
        "input", "gender", "Entrer le sexe du joueur (M/F):", validator=GenderValidator
    ).menu(),
    Interface(
        "input",
        "ranking",
        "Entrer le classement du joueur:",
        validator=PositiveIntegerValidator,
    ).menu(),
]


class PlayerView:
    def get_info():
        player_inputs = prompt(add_player_questions, style=style)
        player_inputs["ranking"] = int(player_inputs["ranking"])
        return player_inputs

    def update_elo_ranking(data):
        for player_id in TableDisplay.display_and_select_players(
            data, 1, "Veuillez selectioner 1 joueur minimun."
        ):
            new_elo = Interface(
                "input",
                "ranking",
                "Entrer le classement du joueur:",
                validator=PositiveIntegerValidator,
            ).menu()
            user_inputs = prompt(new_elo, style=style)
            input_elo = int(user_inputs["ranking"])
            DataController.update_by_id(
                players_table, {"ranking": input_elo}, player_id
            )

    def player_report(data):

        choice = prompt(
            Interface(
                "list",
                "player_rapport_choice",
                "Afficher les joueurs par :",
                choices=["Ordre alphabétique", "Classement"],
            ).menu()
        )
        if choice["player_rapport_choice"] == "Ordre alphabétique":
            table_title = "Joueurs par Ordre alphabétique"
            sorted_players = sorted(
                data, key=lambda d: d["last_name"].upper()
            )
        if choice["player_rapport_choice"] == "Classement":
            table_title = "Joueurs par Classement elo"
            sorted_players = sorted(
                data, key=lambda d: d["ranking"], reverse=True
            )
        while True:
            TableDisplay.display_players(table_title, sorted_players)
            if Interface.confirm("Retouner au menu principal? (O/N)"):
                break


class TableDisplay:
    def display_players(table_title: str, data_from_player_table):
        table = Table(title=table_title)

        table.add_column("Prénom", justify="left", style="#20b7f7")
        table.add_column("Nom", justify="left", style="#20b7f7")
        table.add_column("Naissance", justify="right", style="#ffba0a")
        table.add_column("Sexe", style="#00fa9a")
        table.add_column("Classement", justify="right", style="#d13cd6")
        for player in data_from_player_table:
            table.add_row(
                player["first_name"][:15],
                player["last_name"][:15],
                player["date_of_birth"],
                player["gender"],
                str(player["ranking"]),
            )
        console = Console()
        console.print(table)

    def display_and_select_players(
        data_from_player_table, min_number_of_player: int, error_message: str
    ):

        while True:
            list_player_string = [
                Separator(
                    "{:<18} | {:<16} | {:<10} | {:<5} | {:<10} | {:5}".format(
                        "Prénom", "Nom", "Naissance", "Sexe", "Classment", "ID"
                    )
                )
            ]
            for player in data_from_player_table:
                player_string = (
                    "{:<16} | {:<16} | {:<10} | {:<5} | {:<10} | {:5}".format(
                        player["first_name"][:15],
                        player["last_name"][:15],
                        player["date_of_birth"],
                        player["gender"],
                        player["ranking"],
                        str(player.doc_id),
                    )
                )
                list_player_string.append({"name": player_string})
            select_player = Interface(
                "checkbox",
                "checked",
                "Séléctioner les joueurs :",
                choices=list_player_string,
            ).menu()
            selected_player = prompt(select_player)["checked"]
            selected_player_id = []
            for player in selected_player:
                player_id = int(re.split(r"\|", player)[5])
                selected_player_id.append(player_id)
            if len(selected_player_id) < min_number_of_player:
                print(error_message)
            else:
                break
        return selected_player_id

    def display_players_score(table_title: str, tournament_players: list):
        table = Table(title=table_title)

        table.add_column("Classement", justify="right", style="#f5310a")
        table.add_column("Prénom", justify="left", style="#20b7f7")
        table.add_column("Nom", justify="left", style="#20b7f7")
        table.add_column("Score", style="#00fa9a")
        table.add_column("elo", justify="right", style="#d13cd6")
        i = 1
        for player in tournament_players:
            table.add_row(
                str(i),
                player.first_name[:15],
                player.last_name[:15],
                str(player.score),
                str(player.elo),
            )
            i += 1
        console = Console()
        console.print(table)
