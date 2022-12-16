from typing import Tuple, List, Any
from enum import Enum

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output 

Packet = Tuple[List[Any], List[Any]]
class Comparison(Enum):
    IN_ORDER = 1
    EQUAL = 2
    OUT_ORDER = 3

def parse_input(txt_block: str) -> List[Packet]:
    output = []
    for packets in txt_block.split("\n\n"):
        if len(packets.split("\n")) == 2:
            p1, p2 = packets.split("\n")
            output.append((eval(p1), eval(p2)))
        else:
            p1, p2, _ = packets.split("\n")
            output.append((eval(p1), eval(p2)))

    return output

def compare_nodes(a1: List[Any], a2: List[Any]) -> Comparison:
    p1_iter = iter(a1)
    p2_iter = iter(a2)
    while True:
        i = next(p1_iter, None)
        j = next(p2_iter, None)

        if i == None and j == None:
            return Comparison.EQUAL
        if i == None:
            return Comparison.IN_ORDER
        if j == None:
            return Comparison.OUT_ORDER

        comp = Comparison.EQUAL
        if isinstance(i, List) and isinstance(j, List):
            comp = compare_nodes(i, j)
        elif isinstance(i, int) and isinstance(j, List):
            comp = compare_nodes([i], j)
        elif isinstance(i, List) and isinstance(j, int):
            comp = compare_nodes(i, [j])
        else:
            if i == j:
                comp = Comparison.EQUAL
            elif i < j:
                comp = Comparison.IN_ORDER
            else:
                comp = Comparison.OUT_ORDER
        if comp == Comparison.EQUAL:
            continue
        else:
            return comp

def p1():
    txt_block = read_input("input.txt")
    packets = parse_input(txt_block)
    comps = []
    for packet in packets:
        p1, p2 = packet
        comp = compare_nodes(p1, p2)
        comps.append(comp)
    total = sum([i + 1 for i,j in enumerate(comps) if j == Comparison.IN_ORDER])
    print(f"P1: {total}")

def bubble_sort(packets: List[List[Any]]):
    n = len(packets)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            p1 = packets[j]
            p2 = packets[j+1]
            if compare_nodes(p1, p2) == Comparison.OUT_ORDER:
                swapped = True
                packets[j], packets[j+1] = packets[j+1], packets[j]
        if not swapped:
            return

def p2():
    txt_block = read_input("input.txt")
    packets = parse_input(txt_block)
    packets = [[i, j] for i, j in packets]
    packets = [i for j in packets for i in j]
    packets.append([[2]])
    packets.append([[6]])
    bubble_sort(packets)
    total = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print(f"P2: {total}")

if __name__=="__main__":
    p1()
    p2()
