from datetime import datetime
from logging import raiseExceptions


from models.player import Player
class Round:
    def __init__(self, name, matchs = [], start_datetime = None, end_datetime = None) -> None:
        self.name = name
        self.matchs = matchs
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

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
        matches_list_serialize =[]
        for match in self.matchs:
            temp = tuple(([match[0][0].id_db, match[0][1]], [match[1][0].id_db, match[1][1]]))
            matches_list_serialize.append(temp)
        return({
            'name' : self.name,
            'start_datetime' : self.start_datetime,
            'end_datetime' : self.end_datetime,
            'matchs' : matches_list_serialize
            })

    def deserialize(rounds :list):
        rounds_list = []
        for round in rounds:
            matchs_temp = []
            for match in round['matchs']:
                player1 = Player.instantiate_from_db_by_id(match[0][0])
                player2 = Player.instantiate_from_db_by_id(match[1][0])
                player1.set_score(match[0][1])
                player2.set_score(match[1][1])
                matchs_temp.append((
                    [player1, match[0][1]],
                    [player1, match[1][1]]
                    
                ))
            this_round = Round(
                round['name'],
                start_datetime = round['start_datetime'],
                end_datetime = round['end_datetime'],
                matchs = matchs_temp
                )
            rounds_list.append(this_round)
        return rounds_list
