import copy
from controllers.utilities import is_even


class Round_controller:
    def sort_player_list_by_score_then_elo(player_list):
        return (player_list.sort(key=lambda x: (x.score, x.elo), reverse=True))

    def create_matches_for_first_round(
        players_in_the_tournament: list, first_round: object
    ):
        Round_controller.sort_player_list_by_score_then_elo(players_in_the_tournament)
        if not is_even(len(players_in_the_tournament)):
            players_in_this_round = copy.copy(players_in_the_tournament)
            players_in_this_round.pop().set_score(1)
        else:
            players_in_this_round = copy.copy(players_in_the_tournament)

        for i in range(0, int(len(players_in_this_round) / 2)):
            first_round.register_match(
                players_in_this_round[i],
                players_in_this_round[int(len(players_in_this_round)/2) +(i)],
            )

    def check_if_players_met(player1, player2, rounds):
        """Check if the two players already played each other; return True is they already met; return False if the didn't

        Args:
            player1 (object): [Player instance]
            player2 (object): [Player instance]
            rounds (list): [list of rounds played; should be tournament.rounds]

        Returns:
            [bool]: [return True is they already met;
                        return False if the didn't]
        """
        round_checked = 0
        have_met = False
        while round_checked < len(rounds):
            for round in rounds:
                for match in round.matchs:
                    if match[0][0] == player1: 
                        if match[1][0] == player2:
                            have_met = True  #return have_met = True 
                    elif match[1][0] == player1:
                        if match[0][0] == player2:
                            have_met = True
            round_checked += 1
        return have_met

    def create_matches_for_this_round(
        player_in_the_tournament: list, current_round, rounds
    ):
        Round_controller.sort_player_list_by_score_then_elo(
                player_in_the_tournament)
        available_players = copy.copy(player_in_the_tournament)        
        while len(available_players) > 2:
            i = 1
            match_found = False
            while i < len(available_players) and not match_found:
                if not Round_controller.check_if_players_met(
                    available_players[0], available_players[i], rounds
                ):
                    current_round.register_match(
                        available_players.pop(0), available_players.pop(i - 1)
                    )
                    match_found = True
                i += 1
                if i == len(available_players):
                    current_round.register_match(
                        available_players.pop(0), available_players.pop(0)
                    )
        if len(available_players) == 2:
            current_round.register_match(
                available_players.pop(0), available_players.pop(0)
            )
        if len(available_players) == 1:
            available_players[0].set_score(1)
