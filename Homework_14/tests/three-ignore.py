"""
A, B, B, A, B, A, B, A, A, A, B, B, A, B
A = 28
B = 28
Team A wins by tie breaker (their 6th runner finished 10th and Team Bs 6th runner finished 11th)

"""
import pytest
import src
from src.cross_country_race import Runner, Team, Results, Top5ScoringStrategy, SixthRunnerTieBreakerStrategy
# Test case one 
def test_cross_country_race():
    #Initialize two teams
    team_a = Team("Team A", Top5ScoringStrategy(), SixthRunnerTieBreakerStrategy())
    team_b = Team("Team A", Top5ScoringStrategy(), SixthRunnerTieBreakerStrategy())

    # Add runners to teams
    team_a.add_runner(Runner(1, "Team A"))
    team_a.add_runner(Runner(2, "Team A"))
    team_a.add_runner(Runner(3, "Team A"))
    team_a.add_runner(Runner(4, "Team A"))
    team_a.add_runner(Runner(5, "Team A"))
    team_a.add_runner(Runner(6, "Team A"))
    team_a.add_runner(Runner(7, "Team A"))

    team_b.add_runner(Runner(8, "Team B"))
    team_b.add_runner(Runner(9, "Team B"))
    team_b.add_runner(Runner(10, "Team B"))
    team_b.add_runner(Runner(11, "Team B"))
    team_b.add_runner(Runner(12, "Team B"))

    # Calculate scores for teams
    team_a.calculate_score()
    team_b.calculate_score()

    # Create Results object and add teams
    results = Results()
    results.add_team(team_a)
    results.add_team(team_b)

    # Print placement in finishing order
    results.printPlacement()

    # Determine the winning team
    results.breakTie()

    # Determine the output based on the tie
    if results.teams[0].score < results.teams[1].score:
        print(f"{team_a.name} = {results.teams[0].score}")
        print(f"{team_b.name} = {results.teams[1].score}")
        print(f"Team {results.teams[0].name} wins")
    elif results.teams[0].score > results.teams[1].score:
        print(f"{team_a.name} = {results.teams[0].score}")
        print(f"{team_b.name} = {results.teams[1].score}")
        print(f"Team {results.teams[1].name} wins")
    else:
        tiebreak_teams = [team_a, team_b]
        tiebreak_teams.sort(key=lambda team: team.get_tiebreak_place())
        if tiebreak_teams[0].get_tiebreak_place() == tiebreak_teams[1].get_tiebreak_place():
            print(f"{team_a.name} = {results.teams[0].score}")
            print(f"{team_b.name} = {results.teams[1].score}")
            print(f"It's a tie!")
        else:
            print(f"{team_a.name} = {results.teams[0].score}")
            print(f"{team_b.name} = {results.teams[1].score}")
            print(f"Team {tiebreak_teams[0].name} wins by tiebreaker (their 6th runner finished {tiebreak_teams[0].get_tiebreak_place()} and {tiebreak_teams[1].name}'s 6th runner finished {tiebreak_teams[1].get_tiebreak_place()})")

if __name__ == "__main__":
    pytest.main()
