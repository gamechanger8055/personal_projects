class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.balls_faced = 0
        self.fours = 0
        self.sixes = 0


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.total_score = 0
        self.wickets = 0


class Match:
    def __init__(self, overs, team1, team2):
        self.overs = overs
        self.team1 = team1
        self.team2 = team2
        self.current_batting_team = team1
        self.current_batsmen = [player for player in self.current_batting_team.players]
        self.current_over = 0
        self.current_ball = 0

    def play_ball(self, runs, is_wide, is_no_ball, is_wicket):
        current_batsman = self.current_batsmen[self.current_ball % 2]
        if not is_wide and not is_no_ball:
            current_batsman.score += runs
            current_batsman.balls_faced += 1
            if runs == 4:
                current_batsman.fours += 1
            elif runs == 6:
                current_batsman.sixes += 1
            self.current_batting_team.total_score += runs
            if is_wicket:
                self.current_batting_team.wickets += 1
                self.current_batsmen.pop(self.current_ball % 2)
        self.current_ball += 1

        if self.current_ball % 6 == 0 or is_wide or is_no_ball or is_wicket:
            self.print_scorecard()

    def print_scorecard(self):
        print("\nScorecard for", self.current_batting_team.name)
        print("Player Name\tScore\t4s\t6s\tBalls")

        for player in self.current_batting_team.players:
            strike_marker = "*" if player in self.current_batsmen else ""
            print(f"{player.name}{strike_marker}\t{player.score}\t{player.fours}\t{player.sixes}\t{player.balls_faced}")

        print(
            f"Total: {self.current_batting_team.total_score}/{self.current_batting_team.wickets} Overs: {self.current_over}.{self.current_ball % 6}")

    def simulate_match(self):
        for _ in range(self.overs):
            for _ in range(6):
                runs = int(input("Enter runs scored: "))
                is_wide = False
                is_no_ball = False
                is_wicket = False

                if runs == -1:
                    is_wide = True
                    runs = 1  # Update runs to 1 for a wide ball
                elif runs == -2:
                    is_no_ball = True
                    runs = 1  # Update runs to 1 for a no ball
                elif runs == -3:
                    is_wicket = True
                    runs = 0  # No runs for a wicket

                self.play_ball(runs, is_wide, is_no_ball, is_wicket)

            self.current_over += 1
            self.current_batsmen.reverse()  # Switch the strike
            self.print_scorecard()

        self.print_result()

    def print_result(self):
        if self.team1.total_score > self.team2.total_score:
            winner = self.team1
        else:
            winner = self.team2
        print("\nResult:", winner.name, "won the match by", abs(self.team1.total_score - self.team2.total_score),
              "runs")


if __name__ == "__main__":
    # Create player and team objects for both teams
    team1_players = [Player("P1"), Player("P2"), Player("P3"), Player("P4"), Player("P5")]
    team2_players = [Player("P6"), Player("P7"), Player("P8"), Player("P9"), Player("P10")]

    team1 = Team("Team 1", team1_players)
    team2 = Team("Team 2", team2_players)

    # Create a match object with 2 overs
    match = Match(2, team1, team2)

    # Simulate the match
    match.simulate_match()


class Match:
    # ... (other methods and attributes)

    def simulate_match(self):
        for current_team in [self.team1, self.team2]:
            wickets_fallen = []

            for _ in range(self.overs):
                for _ in range(6):
                    runs = int(input("Enter runs scored: "))
                    is_wide = False
                    is_no_ball = False
                    is_wicket = False

                    if runs == -1:
                        is_wide = True
                        runs = 1  # Update runs to 1 for a wide ball
                    elif runs == -2:
                        is_no_ball = True
                        runs = 1  # Update runs to 1 for a no ball
                    elif runs == -3:
                        is_wicket = True
                        runs = 0  # No runs for a wicket

                    self.play_ball(runs, is_wide, is_no_ball, is_wicket)
                    if is_wicket:
                        wickets_fallen.append(f"{current_team.total_score}-{current_team.wickets}")

                self.current_over += 1
                self.current_batsmen.reverse()  # Switch the strike
                self.print_scorecard()

            self.print_result()

            if wickets_fallen:
                print("\nFall of wickets for", current_team.name, ":", ", ".join(wickets_fallen))

    # ... (other methods)

