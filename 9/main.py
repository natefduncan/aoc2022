from enum import Enum
from typing import List, Tuple

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

Instruction = Tuple[Direction, int]

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_input(txt_block: str) -> List[Instruction]:
    output = []
    for line in txt_block.split("\n"): 
        if line: 
            d_str, move_str = line.split(" ")
            if d_str == "U":
                direction = Direction.UP
            elif d_str == "D":
                direction = Direction.DOWN
            elif d_str == "L":
                direction = Direction.LEFT
            else: 
                direction = Direction.RIGHT
            output.append((direction, int(move_str)))
    return output

Position = Tuple[int, int]

def is_touching(p1: Position, p2: Position) -> bool:
    if p1 == p2:
        return True

    r1, c1 = p1
    r2, c2 = p2
    
    if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
        return True
    else:
        return False

def move_right(p: Position) -> Position:
    row, col = p
    return (row, col + 1)

def move_left(p: Position) -> Position:
    row, col = p
    return (row, col - 1)

def move_up(p: Position) -> Position:
    row, col = p
    return (row + 1, col)

def move_down(p: Position) -> Position:
    row, col = p
    return (row - 1, col)
    
def move_so_touching(head: Position, tail: Position) -> Position:
    if is_touching(head, tail):
        return tail
    else:
        head_row, head_col = head
        tail_row, tail_col = tail
        if head_row == tail_row:
            if head_col - tail_col < 0: # Head is left
                return move_left(tail)
            else:
                return move_right(tail)
        elif head_col == tail_col:
            if head_row - tail_row < 0: # Head is down
                return move_down(tail)
            else:
                return move_up(tail)
        else:
            if head_row - tail_row < 0 and head_col - tail_col < 0: # Head is down left
                return move_left(move_down(tail))
            elif head_row - tail_row > 0 and head_col - tail_col < 0: # Head is up left
                return move_left(move_up(tail))
            elif head_row - tail_row > 0 and head_col - tail_col > 0: # Head is up right 
                return move_right(move_up(tail))
            else:
                return move_right(move_down(tail))

def impl_instruction(positions: List[Position], direction: Direction):
    # Front is head 
    head = positions.pop(0)
    output = []
    if direction == Direction.UP:
        head = move_up(head)
    elif direction == Direction.DOWN:
        head = move_down(head)
    elif direction == Direction.RIGHT:
        head = move_right(head)
    else:
        head = move_left(head)
    output.append(head)
    while True:
        if positions:
            tail = positions.pop(0)
            tail = move_so_touching(head, tail)
            output.append(tail)
            head = tail
        else:
            break
    return output

def p1():
    txt_block = read_input("input.txt")
    instructions = parse_input(txt_block)
    head = (0, 0)
    tail = (0, 0)
    positions = [head, tail]
    tail_positions = []
    tail_positions.append(tail)
    for instruction in instructions:
        direction, move = instruction
        for _ in range(move):
            positions = impl_instruction(positions, direction)
            tail_positions.append(positions[-1])
    total = len(set(tail_positions))
    print(f"P1: {total}")

def debug(positions: List[Position]):
    max_row = max([i[0] for i in positions]) + 1
    max_col = max([i[1] for i in positions]) + 1
    grid = []
    for _ in range(max_row):
        grid.append(["."] * max_col)
    for i, p in enumerate(positions):
        row, col = p
        grid[row][col] = str(i)
    for row in grid:
        print(" ".join(row))
    print("-" * 30)

def p2():
    txt_block = read_input("input.txt")
    instructions = parse_input(txt_block)
    positions = [(0, 0)] * 10
    tail_positions = []
    tail_positions.append((0, 0))
    for instruction in instructions:
        direction, move = instruction
        for _ in range(move):
            positions = impl_instruction(positions, direction)
            tail_positions.append(positions[-1])
    total = len(set(tail_positions))
    print(f"P2: {total}")

def test():
    txt_block = read_input("test.txt")
    instructions = parse_input(txt_block)
    positions = [(6, 11)] * 10
    tail_positions = []
    tail_positions.append((6, 11))
    for instruction in instructions:
        direction, move = instruction
        for _ in range(move):
            positions = impl_instruction(positions, direction)
            #  debug(positions)
            #  input()
            tail_positions.append(positions[-1])
    total = len(set(tail_positions))
    print(f"Test: {total}")
    
if __name__=="__main__":
    p1()
    p2()
    test()
