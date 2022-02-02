from controllers.input_validation import *
from models.template import *

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
    Interface("input", "time_format", "Entrer le format de contrôle du temps:").menu(),
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
    def display_tournament(table_title : str, tournaments : list):
        table = Table(title=table_title)
        
        table.add_column("ID",justify="right", style="#f5310a")
        table.add_column("Nom",justify="right", style="#f5310a")
        table.add_column("Lieu", justify="left", style="#20b7f7")
        table.add_column("Date début", justify="left", style="#20b7f7")
        table.add_column("Nombre de ronde",style="#00fa9a")
        table.add_column("Ronde jouées",justify="right", style="#d13cd6")
        table.add_column("Joueurs",justify="right", style="#d13cd6")
        i = 1
        for tournament in tournaments:
            table.add_row(
                    str(i),
                    player.first_name[:15],
                    player.last_name[:15],
                    str(player.score),
                    str(player.elo)
            )
            i += 1
        console = Console()
        console.print(table)
# for player in this_tournament.players:
#     print(f'id : {player.id_db}| score : {player.score} | elo {player.elo}')
