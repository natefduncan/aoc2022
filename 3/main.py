import itertools
from typing import Tuple, Iterator

def read_file(path):
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_compartments(sack) -> Tuple[str, str]:
    first, second = sack[:len(sack)//2],sack[len(sack)//2:]
    return (first, second)

def parse_sacks(txt_block) -> list[Tuple[str, str]]:
   return [parse_compartments(sack) for sack in txt_block.split("\n") if sack]

def score_item(item) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38 

def parse_intersection(sack):
    a, b = sack
    a = set(list(a))
    b = set(list(b))
    return list(a.intersection(b))

def parse_intersection2(group):
    a, b, c = group 
    a = set(list(a))
    b = set(list(b))
    c = set(list(c))
    return list(a.intersection(b).intersection(c))

def grouper(iterator: Iterator, n: int) -> Iterator[list]:
    while chunk := list(itertools.islice(iterator, n)):
        yield chunk

def p1():
    txt_block = read_file("input.txt")
    sacks = parse_sacks(txt_block)
    intersections = list(map(parse_intersection, sacks))
    flat_intersections = [i for j in intersections for i in j]
    total = sum(list(map(score_item, flat_intersections)))
    print(f"P1: {total}")

def p2():
    txt_block = read_file("input.txt")
    #  sacks = parse_sacks(txt_block)
    groups = list(grouper(iter([i for i in txt_block.split("\n") if i]), 3))
    intersections = map(parse_intersection2, groups)
    flat_intersections = [i for j in intersections for i in j]
    total = sum(list(map(score_item, flat_intersections)))
    print(f"P2: {total}")

if __name__=="__main__":
    p1()
    p2()
