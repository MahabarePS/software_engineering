import pytest
import src
from src.cross_country_race import Runner, Team, Results

def test_create_team():
    # Test if a new team is created correctly with initial properties.
    team = Team("Team A")
    assert team.name == "Team A"
    assert len(team.runners) == 0
    assert team.score == 0

def test_add_runner():
    # Test if adding a runner to a team updates the runners' list correctly.
    team = Team("Team A")
    runner = Runner(1, "Team A")
    team.add_runner(runner)
    assert len(team.runners) == 1

def test_add_runner_max_limit():
    # Test if a team can accept runners up to the maximum limit.
    team = Team("Team A")
    for place in range(1, 8):
        runner = Runner(place, "Team A")
        team.add_runner(runner)
    assert len(team.runners) == 7

def test_calculate_winner():
    # Test if the correct team is identified as the winner.
    team_a = Team("Team A")
    team_b = Team("Team B")
    team_a.score = 25
    team_b.score = 30
    results = Results()
    results.add_team(team_a)
    results.add_team(team_b)
    results.breakTie()
    assert results.teams[0].name == "Team A"

def test_valid_team_creation():
    # Test if teams can be created with valid names.
    team_a = Team("Team A")
    team_b = Team("Team B")
    assert team_a.name == "Team A"
    assert team_b.name == "Team B"

def test_valid_team_no_runners():
    # Test if teams with no runners raise ValueError when calculating scores.
    with pytest.raises(ValueError):
        team_a = Team("Team A")
        team_a.calculate_score()

    with pytest.raises(ValueError):
        team_b = Team("Team B")
        team_b.calculate_score()

def test_team_with_less_runners():
    # Test if a team with fewer than 5 runners raises an error when calculating scores.
    team_a = Team("Team A")
    team_b = Team("Team B")

    for place in range(1, 5):
        runner = Runner(place, "Team A")
        team_a.add_runner(runner)
    with pytest.raises(ValueError):
        team_a.calculate_score()

    for place in range(1, 5):
        runner = Runner(place, "Team B")
        team_b add_runner(runner)
    with pytest.raises(ValueError):
        team_b.calculate_score()

def test_lower_case_runner_placement():
    # Test if placing runners with lower case values raises ValueError.
    with pytest.raises(ValueError):
        runner = Runner("a", "Team A")

    with pytest.raises(ValueError):
        runner = Runner("b", "Team B")

def test_empty_team_names():
    # Test if creating teams with empty names raises ValueError.
    with pytest.raises(ValueError):
        team_a = Team("")

    with pytest.raises(ValueError):
        team_b = Team(" ")

if __name__ == "__main__":
    import pytest
    pytest.main()