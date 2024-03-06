class CricketMatch:
    def __init__(self, overs, team1, team2):
        self.teams=[team1,team2]
        self.overs = overs
        self.team1 = team1
        self.team2 = team2
        self.current_over = 0
        self.current_ball = 0
        self.current_batting_team = self.teams[self.current_over // self.overs]
        self.current_batsmen = [player for player in self.current_batting_team.players]

    def current_teams(self):
        current_team=[self.team1, self.team2]
        p=self.current_over//self.overs
        self.current_batting_team = current_team[p]

    def current_batsmans(self):
        self.current_batsmen = [player for player in self.current_batting_team.players]

    def batsman_change(self, runs, current_batsman):
        if runs in [1,3] or self.current_ball%6==1:
            current_batsman = self.current_batsmen[self.current_ball % 2]
        return current_batsman

    def play_ball(self, runs, is_wide, is_no_ball, is_wicket):
        if len(self.current_batsmen)>1:
            current_batsman = self.current_batsmen[self.current_ball % 2]
            current_batsman=self.batsman_change(runs,current_batsman)
        if is_wide or is_no_ball:
            self.current_batting_team.total_score+=1
        else:
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

        if self.current_ball % 6 == 0:
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
        self.current_batsmans()
        self.current_teams()
        for current_team in [self.team1, self.team2]:
            players=current_team.players
            print("Scorecard for: "+ str(current_team.name))
            wickets_fallen =[]
            for _ in range(self.overs):
                i=0
                while i<6:
                    runs = input("Enter runs scored: ")
                    is_wide = False
                    is_no_ball = False
                    is_wicket = False

                    if runs == "Wd":
                        is_wide = True
                        i-=1
                        runs = 1  # Update runs to 1 for a wide ball
                    elif runs == "Nb":
                        is_no_ball = True
                        i-=1
                        runs = 1  # Update runs to 1 for a no ball
                    elif runs == "W":
                        is_wicket = True
                        runs = 0  # No runs for a wicket
                    self.play_ball(int(runs), is_wide, is_no_ball, is_wicket)
                    i+=1
                    if is_wicket:
                        wickets_fallen.append(f"{current_team.total_score}-{current_team.wickets}")


                self.current_over += 1
                self.current_batsmen.reverse()  # Switch the strike
                self.print_scorecard()
                if wickets_fallen:
                    print("\nFall of wickets for", current_team.name, ":", ", ".join(wickets_fallen))

        self.print_result()

    def print_result(self):
        if self.team1.total_score > self.team2.total_score:
            winner = self.team1
        else:
            winner = self.team2
        print("\nResult:", winner.name, "won the match by", abs(self.team1.total_score - self.team2.total_score),
              "runs")
