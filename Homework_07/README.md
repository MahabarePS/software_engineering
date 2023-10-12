# Cross Country Running Race Scoring

This Python program calculates the score of a cross country running race based on the provided input. The code uses object-oriented principles to define the data structure for scoring cross country teams. It allows you to input data for two teams and calculates the scores, breaking ties if necessary.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Running the Tests](#running-the-tests)

## Features

- Create and manage cross country teams (Team and Runner classes).
- Input the place of each runner for two teams.
- Calculate and compare team scores.
- Handle tie-breaking based on the place of the 6th runner.
- Detailed results with team scores and the winning team.

## Requirements

- Python 3.11.1

## Usage

To run the program, follow these steps:

1. Navigate to the source directory:
   ```bash
   $ cd .\src\
   $ python .\cross_country_race.py
2. To run the tests for this program, you need to use the pytest library. Here's how you can run the tests:
3.  Install pytest using pip if you haven't already:
    $ pip install pytest
4.  Navigate to the tests directory:
    $ cd ..  # Move up one level
    $ cd .\tests\
5.  Run the tests with pytest:
    $ pytest one.py