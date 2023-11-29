"""
University: Purdue University Fort Wayne
Semester: Fall 2023
Class: ACS560
Professor: Matthew Parker
Assignment: Homework_07
Goal: Think outside the box to test the stability of your program by creating relevant test cases
Submited by: Prasad Sadanand Mahabare
"""
from abc import ABC, abstractmethod

# Define Strategy interfaces
class ScoringStrategy(ABC):
    @abstractmethod
    def calculate_score(self, runners):
        pass

class TieBreakerStrategy(ABC):
    @abstractmethod
    def get_tiebreak_place(self, runners):
        pass

# Implement concrete strategies
class Top5ScoringStrategy(ScoringStrategy):
    def calculate_score(self, runners):
        top_5_runners = sorted(runners, key=lambda x: x.place)[:5]
        return sum(runner.place for runner in top_5_runners)

class SixthRunnerTieBreakerStrategy(TieBreakerStrategy):
    def get_tiebreak_place(self, runners):
        if len(runners) >= 6:
            return min(runners, key=lambda x: x.place).place
        else:
            return None

# An individual that will have a place and be a member of a Team
class Runner:
    def __init__(self, place, member_of_team):
        if not str(place).isnumeric():
            raise ValueError("Runner's place must be a numeric value.")
        self.place = place
        self.member_of_team = member_of_team

# Consisting of its Athletes, points scored, and overall finish
class Team:
    # Initially zero score and no athletes/runners
    def __init__(self, name, scoring_strategy, tie_breaker_strategy):
        if not name.strip():  # Check for an empty name
            raise ValueError("Team name cannot be empty.")
        self.runners = []
        self.score = 0
        self.name = name
        self.scoring_strategy = scoring_strategy
        self.tie_breaker_strategy = tie_breaker_strategy

    # Append runners (limited to 5-7 runners)
    def add_runner(self, runner):
        if len(self.runners) < 7:
            self.runners.append(runner)
        elif len(self.runners) < 5:
            raise ValueError("A team must have at least 5 runners.")
        else:
            raise ValueError("A team cannot have more than 7 runners.")

    # Append team_score
    def calculate_score(self):
        # Teams that do not have at least 5 runners are not scored as a team.
        if len(self.runners) < 5:
            self.score = 0
            raise ValueError("Teams that do not have at least 5 runners are not scored as a team.")
        self.score = self.scoring_strategy.calculate_score(self.runners)

    # Check if there is a 6th runner for tie-breaking
    def get_tiebreak_place(self):
        return self.tie_breaker_strategy.get_tiebreak_place(self.runners)

    def __str__(self):
        return f"Team with score {self.score} - {self.name}"

# List of all teams in their finishing order
class Results:
    def __init__(self):
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    # Sort teams by their scores (lower score is better)
    def printPlacement(self):
        for i, team in enumerate(self.teams, start=1):
            print(f"{i}. {team}: {team.name}")

    # Sort teams by their scores and tie-breaker places (lower score is better)
    def breakTie(self):
        self.teams.sort(key=lambda team: (team.name, team.get_tiebreak_place()))
        return self.teams

def main():
    team_a_name = input("Enter the name for Team A: ")
    team_b_name = input("Enter the name for Team B: ")

    # Create instances of strategies
    top_5_strategy = Top5ScoringStrategy()
    sixth_runner_strategy = SixthRunnerTieBreakerStrategy()

    # Instantiate teams with respective strategies
    team_a = Team(team_a_name, top_5_strategy, sixth_runner_strategy)
    team_b = Team(team_b_name, top_5_strategy, sixth_runner_strategy)

    while True:
        print(f"Enter runner information for {team_a_name} or {team_b_name} (5-7 runners):")
        
        try:
            place = int(input("Runner's Place (integer): "))
            team_name = input(f"Enter 'A' for {team_a_name} or 'B' for {team_b_name} or 'done'): ")
            
            if team_name == 'A':
                team_a.add_runner(Runner(place, team_a_name))
            elif team_name == 'B':
                team_b.add_runner(Runner(place, team_b_name))
            elif team_name == 'done':
                break
            else:
                print(f"Invalid team name. Enter 'A' for {team_a_name} or 'B' for {team_b_name} or 'done'): ")
        except ValueError:
            print("Invalid input. Place must be an integer.")

    team_a.calculate_score()
    team_b.calculate_score()

    results = Results()
    results.add_team(team_a)
    results.add_team(team_b)

    results.printPlacement()
    results.breakTie()

    if results.teams[0].score < results.teams[1].score:
        print(f"{team_a_name} = {results.teams[0].score}")
        print(f"{team_b_name} = {results.teams[1].score}")
        print(f"Team {results.teams[0].name} wins")
    elif results.teams[0].score > results.teams[1].score:
        print(f"{team_a_name} = {results.teams[0].score}")
        print(f"{team_b_name} = {results.teams[1].score}")
        print(f"Team {results.teams[1].name} wins")
    else:
        tiebreak_teams = [team_a, team_b]
        tiebreak_teams.sort(key=lambda team: team.get_tiebreak_place())
        if tiebreak_teams[0].get_tiebreak_place() == tiebreak_teams[1].get_tiebreak_place():
            print(f"{team_a_name} = {results.teams[0].score}")
            print(f"{team_b_name} = {results.teams[1].score}")
            print(f"It's a tie!")
        else:
            print(f"{team_a_name} = {results.teams[0].score}")
            print(f"{team_b_name} = {results.teams[1].score}")
            print(f"Team {tiebreak_teams[0].name} wins by tiebreaker (their 6th runner finished {tiebreak_teams[0].get_tiebreak_place()} and {tiebreak_teams[1].name}'s 6th runner finished {tiebreak_teams[1].get_tiebreak_place()})")

if __name__ == "__main__":
    main()