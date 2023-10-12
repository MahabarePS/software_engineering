"""
A, A, A, A, A, A, A, B, B, B, B, B
A = 15
B = 50
Team A wins

"""
import pytest
from src.cross_country_race import Runner, Team, Results

# Test case one 
def test_cross_country_race():
    #Initialize two teams
    team_a = Team()
    team_b = Team()

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
    if results.teams[0].score < results.teams[1].score:
        print(f"Team {results.teams[0]} wins")
    elif results.teams[0].score > results.teams[1].score:
        print(f"Team {results.teams[1]} wins")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    pytest.main()
