from datetime import datetime
from logging import raiseExceptions


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
