from typing import Tuple, Optional, List

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

Instruction = Tuple[str, Optional[int], int]

def parse_input(txt_block: str) -> List[Instruction]:
    output = []
    for line in txt_block.split("\n"):
        if line:
            if line == "noop": 
                output.append(("noop", None, 1))
            else:
                _, amount = line.split(" ")
                output.append(("addx", int(amount), 2))
    return output

def evaluate(instruction: Instruction, clock: int, register: int) -> List[Tuple[int, int]]:
    _, value, cycles = instruction
    value = value if value else 0
    signals = []
    for _ in range(cycles):
        cycles -= 1
        clock += 1
        if cycles == 0:
            register += value
        signals.append((clock, register))
    return signals

def impl_clock(instructions: List[Instruction]) -> List[Tuple[int, int]]:
    register = 1 
    clock = 0 
    signals = []
    for i in instructions:
        signals += evaluate(i, clock, register)
        clock, register = signals[-1]
    return signals

def draw(register: int, pixel: int) -> str:
    if abs(pixel - register) <= 1:
        return "#"
    else:
        return "."

def p1():
    txt_block = read_input("input.txt")
    instructions = parse_input(txt_block)
    signal = impl_clock(instructions)
    total = 0
    for i in range(19, len(signal), 40):
        clock, register = signal[i-1]
        total += (clock + 1) * register
    print(f"P1: {total}")

def p2():
    txt_block = read_input("input.txt")
    instructions = parse_input(txt_block)
    signal = impl_clock(instructions)
    output = ""
    for i in range(0, len(signal), 40):
        line = ""
        for pixel in range(40):
            _, register = signal[i + pixel - 1]
            line += draw(register, pixel)
        line += "\n"
        output += line
    print(f"P2:\n {output}")

if __name__=="__main__":
    p1()
    p2() 
