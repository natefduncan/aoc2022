from __future__ import annotations
from typing import Optional, List
import math
from tqdm import tqdm
import sys
sys.set_int_max_str_digits(0)

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

class Monkey:
    def __init__(self, items: List[int], divisible_by: int, divisible_true: int, divisible_false: int, operation: str, lh: str, rh: str):
        self.items = items
        self.divisible_by = divisible_by
        self.divisible_true = divisible_true
        self.divisible_false = divisible_false
        self.operation = operation
        self.lh = lh
        self.rh = rh
    
    def inspect_item(self, item: int) -> int:
        #  print(f"Inspecting {item}")
        lh = item if self.lh == "old" else int(self.lh)
        rh = item if self.rh == "old" else int(self.rh)
        if self.operation == "*":
            return lh * rh
        elif self.operation == "+":
            return lh + rh
        else:
            return lh - rh

    def test_item(self, item: int) -> int:
        if item % self.divisible_by == 0:
            return self.divisible_true
        else:
            return self.divisible_false

    def inspect_items(self, monkeys: List[Monkey]) -> int:
        processed = 0
        while True:
            item = self.get_item()
            if item:
                new_item = self.inspect_item(item)
                new_item = int(math.floor(new_item // 3)) # P1
                new_monkey = self.test_item(new_item)
                monkeys[new_monkey].add_item(new_item)
                processed += 1
            else:
                break
        return processed

    def inspect_items2(self, monkeys: List[Monkey]) -> int:
        processed = 0
        lcm = math.lcm(*[i.divisible_by for i in monkeys])
        while True:
            item = self.get_item()
            if item:
                new_item = self.inspect_item(item)
                new_item = new_item % lcm
                new_monkey = self.test_item(new_item)
                monkeys[new_monkey].add_item(new_item)
                processed += 1
            else:
                break
        return processed

    def get_item(self) -> Optional[int]:
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def add_item(self, item: int):
        self.items.append(item)

def parse_monkeys(txt_block: str) -> List[Monkey]:
    lines = iter(txt_block.split("\n"))
    monkeys = []
    data = {}
    while True:
        try:
            line = next(lines)
            if "Starting" in line:
                data["items"] = [int(i) for i in line.split(":")[1].strip().split(",")]
            elif "Operation" in line:
                lh, operation, rh = line.split("=")[1].strip().split(" ")
                data["lh"] = lh
                data["operation"] = operation
                data["rh"] = rh
            elif "Test" in line:
                data["divisible_by"] = int(line.split(" ")[-1])
                line = next(lines)
                data["divisible_true"] = int(line.split(" ")[-1])
                line = next(lines)
                data["divisible_false"] = int(line.split(" ")[-1])
                monkeys.append(Monkey(**data))
                data = {}
            else:
                continue
        except:
            break
    return monkeys

def p1():
    txt_block = read_input("input.txt")
    monkeys = parse_monkeys(txt_block)
    inspected = [0] * len(monkeys)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            inspected[i] += monkey.inspect_items(monkeys)
    #  for i, monkey in enumerate(monkeys):
        #  print(f"{i}: {monkey.items}")
    monkey_business = sorted(inspected, reverse = True)[0] * sorted(inspected, reverse = True)[1]
    print(f"P1: {monkey_business}")

# Modulo congruence is preserved for multiplication and addition operations
def p2():
    txt_block = read_input("input.txt")
    monkeys = parse_monkeys(txt_block)
    inspected = [0] * len(monkeys)
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            inspected[i] += monkey.inspect_items2(monkeys)
    monkey_business = sorted(inspected, reverse = True)[0] * sorted(inspected, reverse = True)[1]
    print(f"P2: {monkey_business}")

if __name__=="__main__":
    p1()
    p2()
