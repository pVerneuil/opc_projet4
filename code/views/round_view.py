from models.template import *

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