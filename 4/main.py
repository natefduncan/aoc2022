from typing import Tuple, Iterable, List

Pair = Tuple[Iterable[int], Iterable[int]]

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_pair(pair_str: str) -> Pair: 
    a, b = pair_str.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    return (range(int(a1), int(a2)+1), range(int(b1), int(b2)+1))

def contains_all_subset(l1: Iterable[int], l2: Iterable[int]):
   return all([i in l2 for i in l1]) or all([i in l1 for i in l2])

def contains_any_subset(l1: Iterable[int], l2: Iterable[int]):
   return any([i in l2 for i in l1])

def parse_pairs(txt_block: str) -> List[Pair]:
    return [parse_pair(i) for i in txt_block.split("\n") if i]

def p1():
    txt_block = read_input("input.txt")
    pairs = parse_pairs(txt_block)
    total = sum([contains_all_subset(a, b) for a, b in pairs])
    print(f"P1: {total}")

def p2():
    txt_block = read_input("input.txt")
    pairs = parse_pairs(txt_block)
    total = sum([contains_any_subset(a, b) for a, b in pairs])
    print(f"P2: {total}")

if __name__=="__main__":
    p1()
    p2()
