from typing import List, Tuple

Instruction = Tuple[int, int, int]

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_instruction(instruction_str: str) -> Instruction:
    return tuple([int(i) for i in instruction_str.split(" ") if i.isnumeric()])

def parse_instructions(input: str) -> List[Instruction]:
    return [parse_instruction(i) for i in input.split("\n") if i]

def move(data: List[List[str]], from_: int, to_: int):
    crate = data[from_-1].pop()
    data[to_-1].append(crate)

def move_blocks(data: List[List[str]], amount: int, from_: int, to_: int):
    crates = []
    for _ in range(amount):
        crates.append(data[from_-1].pop())
    data[to_-1] += crates[::-1]

def execute_instructions(data: List[List[str]], instructions: List[Instruction]):
    for instruction in instructions:
        amount, from_, to_ = instruction
        for _ in range(amount):
            move(data, from_, to_)

def p1():
    data = [
       ["B", "P", "N", "Q", "H", "D", "R", "T"], 
       ["W", "G", "B", "J", "T", "V"], 
       ["N", "R", "H", "D", "S", "V", "M", "Q"], 
       ["P", "Z", "N", "M", "C"], 
       ["D", "Z", "B"], 
       ["V", "C", "W", "Z"], 
       ["G", "Z", "N", "C", "V", "Q", "L", "S"], 
       ["L", "G", "J", "M", "D", "N", "V"], 
       ["T", "P", "M", "F", "Z", "C", "G"]
    ]
    txt_block = read_input("input.txt")
    instructions = parse_instructions(txt_block)
    execute_instructions(data, instructions)
    output = "".join([i[-1] for i in data])
    print(f"P1: {output}")

def p2():
    data = [
       ["B", "P", "N", "Q", "H", "D", "R", "T"], 
       ["W", "G", "B", "J", "T", "V"], 
       ["N", "R", "H", "D", "S", "V", "M", "Q"], 
       ["P", "Z", "N", "M", "C"], 
       ["D", "Z", "B"], 
       ["V", "C", "W", "Z"], 
       ["G", "Z", "N", "C", "V", "Q", "L", "S"], 
       ["L", "G", "J", "M", "D", "N", "V"], 
       ["T", "P", "M", "F", "Z", "C", "G"]
    ]
    txt_block = read_input("input.txt")
    instructions = parse_instructions(txt_block)
    for instruction in instructions:
        amount, from_, to_ = instruction
        move_blocks(data, amount, from_, to_)
    output = "".join([i[-1] for i in data])
    print(f"P2: {output}")

if __name__=="__main__":
    p1()
    p2()
