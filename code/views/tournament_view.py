from views.player_view import PlayerView
from views.template import Interface
from controllers.input_validation import (
    StringValidator,
    DateValidator,
    PositiveIntegerValidator,
)
from controllers.data_controller import DataController, players_table, tournament_table
from rich.console import Console
from rich.table import Table
from PyInquirer import prompt

create_tournament_questions = [
    Interface(
        "input", "name", "Entrer le Nom du tournois:", validator=StringValidator
    ).menu(),
    Interface(
        "input",
        "venue",
        "Entrer le lieu ou se déroule le tournois: ",
        validator=StringValidator,
    ).menu(),
    Interface(
        "input",
        "starting_date_tournament",
        "Entrer la date de début du tournois (JJ/MM/AAAA):",
        validator=DateValidator,
    ).menu(),
    Interface("input", "time_format", "Entrer la cadence:").menu(),
    Interface(
        "input", "description", "Entrer une rapide description du tournois: "
    ).menu(),
    Interface(
        "input",
        "number_of_rounds",
        "Entrer le nombre de ronde",
        validator=PositiveIntegerValidator,
    ).menu(),
]


class TournamentView:
    def display_tournaments(tournaments: list, table_title: str, display_players=False):
        """display tournaments in a table

        Args:
            table_title (str): displayed title of the tables
            tournaments (list): list of dictionaries from the database
            display_players (bool, optional): True to display players in tounaments. Defaults to False.
        """
        table = Table(title=table_title, show_lines=True)

        table.add_column("ID", justify="right", style="#f5310a")
        table.add_column("Nom", justify="left", style="#f5310a")
        table.add_column("Lieu", justify="left", style="#20b7f7")
        table.add_column("Date début", justify="left", style="#20b7f7")
        table.add_column("Cadence", justify="left", style="#20b7f7")
        table.add_column("Description", justify="left", style="#20b7f7")
        table.add_column("Nombre \nde ronde", justify="center", style="#00fa9a")
        table.add_column("Ronde \njouées", justify="center", style="#d13cd6")
        if display_players:
            table.add_column("Joueurs", justify="right", style="#d13cd6")

        for tournament in tournaments:
            if display_players:
                players = []
                for id in tournament["players"]:
                    player = DataController.get_document_by_id(players_table, id)
                    players.append(
                        f"{player['first_name'][:15]} {player['last_name'][:15]}"
                    )
                table.add_row(
                    str(tournament.doc_id),
                    tournament["name"],
                    tournament["venue"],
                    tournament["starting_date_tournament"],
                    tournament["time_format"],
                    tournament["description"][:40],
                    str(tournament["number_of_rounds"]),
                    str(tournament["number_of_rounds_played"]),
                    "\n".join(players),
                )
            else:
                table.add_row(
                    str(tournament.doc_id),
                    tournament["name"],
                    tournament["venue"],
                    tournament["starting_date_tournament"],
                    tournament["time_format"],
                    tournament["description"][:40],
                    str(tournament["number_of_rounds"]),
                    str(tournament["number_of_rounds_played"]),
                )
        console = Console()
        console.print(table)

    def display_and_select_tournament(
        tournaments: list,
        table_title: str,
        selection_message: str,
        display_players=False,
    ):

        """display tournament and allow to select one, returns the id of the selected tournament

        Args:
            tournaments (list): list of tournaments to display
            table_title (str): title on top of the table by
            selection_message (str): message displayed before selections
            display_players (bool): True to display player. Default to False

        Returns:
            [int]: [selected tournament id]
        """
        tournaments_ids = []
        for tournament in tournaments:
            tournaments_ids.append(str(tournament.doc_id))
        TournamentView.display_tournaments(tournaments, table_title, display_players)
        list_to_select_from = Interface(
            "list", "selected_tournament", selection_message, choices=tournaments_ids
        ).menu()
        return int(prompt(list_to_select_from)["selected_tournament"])

    def report_players_in_tournament():
        all_tournaments_data = DataController.fetch_all_data_from_table(
            tournament_table
        )
        selected_tournament_id = TournamentView.display_and_select_tournament(
            all_tournaments_data,
            "Tournois enregistés",
            "Selection l'id d'un tournois pour en afficher les joueurs:",
        )
        selected_tournament = DataController.get_document_by_id(
            tournament_table, selected_tournament_id
        )
        PlayerView.player_report(
            DataController.get_documents_by_ids(
                players_table, selected_tournament["players"]
            )
        )
