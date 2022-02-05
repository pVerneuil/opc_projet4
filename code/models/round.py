from datetime import datetime


class Round:
    def __init__(self, name) -> None:
        self.name = name
        self.matchs = []

    def register_match(self, joueur1: object, joueur2: object) -> None:
        match = tuple(([joueur1, 0], [joueur2, 0]))
        self.matchs.append(match)

    def set_date_and_time(self, starting: bool):
        """set the date and time for a round.

        Args:
            starting (bool): Set True for start of round; False for end of round
        """
        if starting:
            self.start_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if not starting:
            self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if type(starting) != bool:
            raise TypeError(
                "can only take True or False (True to set the starting date&time; Fasle to set the end date&time)"
            )

    def serialize(self):
        matches_list_serialize = []
        for match in self.matchs:
            temp = tuple(
                ([match[0][0].id_db, match[0][1]], [match[1][0].id_db, match[1][1]])
            )
            matches_list_serialize.append(temp)
        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matchs": matches_list_serialize,
        }

    def deserialize(round: list, players: list):
        matchs = []
        for match in round["matchs"]:
            match_temp = list(range(2))
            for player in players:
                if getattr(player, "id_db") == match[0][0]:
                    player.set_score(match[0][1])
                    match_temp[0] = [player, match[0][1]]
                if getattr(player, "id_db") == match[1][0]:
                    player.set_score(match[1][1])
                    match_temp[1] = [player, match[1][1]]
            matchs.append(tuple(match_temp))
        this_round = Round(round["name"])
        this_round.start_datetime = (round["start_datetime"],)
        this_round.end_datetime = (round["end_datetime"],)
        this_round.matchs = matchs
        return this_round
