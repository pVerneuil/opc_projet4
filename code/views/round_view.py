class RoundView:
    def disply_matches_in_this_round(round):
        for match in round.matchs:
            print(
                f"{match[0][0].first_name} {match[0][0].last_name} contre {match[1][0].first_name} {match[1][0].last_name}"
            )
