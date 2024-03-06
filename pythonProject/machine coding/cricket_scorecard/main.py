from player import Player
from team import Team
from cricket_match import CricketMatch
def main():
    players=int(input("Number of players in each team: "))
    team1 =["P"+str(i) for i in range(1,players+1)]
    team2 =["P"+str(i) for i in range(players+1,2*players+1)]
    team1_players = [Player(team) for team in team1]
    team2_players = [Player(team) for team in team2]

    overs= int(input("Number of overs: "))
    team1 = Team("Team 1", team1_players)
    team2 = Team("Team 2", team2_players)

    # Create a match object with 2 overs
    match = CricketMatch(overs, team1, team2)

    # Simulate the match
    match.simulate_match()

main()