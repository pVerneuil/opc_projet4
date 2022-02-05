from controllers.data_controller import DataController, players_table
import random


class Testing:
    def add_many_fake_player_to_db(a: int):
        i = 1
        dict = []
        for y in range(0, a):
            b = 2000 + i
            c = 1000 + i
            dict.append(
                {
                    "first_name": f"John{i}",
                    "last_name": f"Doe{i}",
                    "date_of_birth": f"01/01/{b}",
                    "gender": "M",
                    "ranking": int(f"{c}"),
                }
            )
            i += 1
        DataController.add_many_to_db(dict, players_table)

    def random_round_result(round: object):
        for match in round.matchs:
            r = random.randrange(0, 3, 1)
            match[0][1] = r / 2
            match[0][0].set_score(r / 2)
            match[1][1] = 1 - r / 2
            match[1][0].set_score(1 - r / 2)
