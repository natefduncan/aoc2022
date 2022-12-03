from enum import IntEnum
from typing import List, Tuple

class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6

def get_txt_block(path):
    with open(path, "r") as f:
        block = f.read()
    return block

def parse_shape(shape_str):
    if shape_str in "AX":
        return Shape.ROCK
    elif shape_str in "BY":
        return Shape.PAPER
    else:
        return Shape.SCISSORS

def parse_outcome(game_tuple):
    a, b = game_tuple
    if a == b:
        return Outcome.DRAW
    if a == Shape.ROCK:
        return Outcome.WIN if b == Shape.PAPER else Outcome.LOSE
    elif a == Shape.PAPER:
        return Outcome.WIN if b == Shape.SCISSORS else Outcome.LOSE
    else:
        return Outcome.WIN if b == Shape.ROCK else Outcome.LOSE

def parse_outcome_str(x):
    if x in "X":
       return Outcome.LOSE
    elif x in "Y":
        return Outcome.DRAW
    else:
        return Outcome.WIN

def parse_games(txt_block: str) -> list[tuple[Shape, Shape]]:
    output = []
    for game_str in txt_block.split("\n"):
        if game_str:
            game = tuple(map(parse_shape, game_str.split(" ")))
            output.append(game)
    return output

# There's got to be a more elegant way to do this
def shape_from_outcome(game: tuple[Shape, Outcome]) -> Shape:
    shape, outcome = game
    if outcome == Outcome.DRAW:
        return shape
    if shape == Shape.ROCK:
        return Shape.PAPER if outcome == Outcome.WIN else Shape.SCISSORS
    elif shape == Shape.SCISSORS:
        return Shape.ROCK if outcome == Outcome.WIN else Shape.PAPER
    else:
        return Shape.SCISSORS if outcome == Outcome.WIN else Shape.ROCK

def parse_games2(txt_block: str) -> list[tuple[Shape, Outcome]]:
    output = []
    for game_str in txt_block.split("\n"):
        if game_str:
            a, b = game_str.split(" ")
            a = parse_shape(a)
            b = parse_outcome_str(b)
            game = (a, b)
            output.append(game)
    return output

def parse_outcomes(games: list[tuple[Shape, Shape]]) -> list[Outcome]:
    return list(map(parse_outcome, games))

def parse_score(game, outcome):
    return sum([game[1], outcome])

def p1():
    txt_block = get_txt_block("input.txt")
    games = parse_games(txt_block)
    outcomes = parse_outcomes(games)
    total = sum([parse_score(game, outcome) for game, outcome in zip(games, outcomes)])
    print(f"P1: {total}")

def p2():
    txt_block = get_txt_block("input.txt")
    games = parse_games2(txt_block)
    shapes = [shape_from_outcome(game) for game in games]
    total = sum([game[1] + shape for game, shape in zip(games, shapes)])
    print(f"P2: {total}")

if __name__=="__main__":
    p1()
    p2()
