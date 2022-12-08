from typing import List

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def p1():
    txt_block = read_input("input.txt")
    chars = list(txt_block)
    for i in range(4, len(chars)):
        if len(set(chars[(i-4):i])) == 4:
            print(f"P1: {i}")
            break

def p2():
    txt_block = read_input("input.txt")
    chars = list(txt_block)
    for i in range(14, len(chars)):
        if len(set(chars[(i-14):i])) == 14:
            print(f"P2: {i}")
            break

if __name__=="__main__":
    p1()
    p2()
