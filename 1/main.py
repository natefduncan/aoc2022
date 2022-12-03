def get_txt_block(path):
    with open(path, "r") as f:
        txt_block = f.read()
    return txt_block

def get_elves(txt_block):
    return txt_block.split("\n\n") 

def get_calories(elves):
    return [sum([int(calorie) for calorie in elf.split("\n") if calorie]) for elf in elves]

def p1():
    txt_block = get_txt_block("input.txt")
    elves = get_elves(txt_block)
    calories = get_calories(elves)
    print(f'P1: {max(calories)}')

def p2():
    txt_block = get_txt_block("input.txt")
    elves = get_elves(txt_block)
    calories = sorted(get_calories(elves), reverse = True)
    print(f"P2: {sum(calories[:3])}")

if __name__=="__main__":
    p1()
    p2()
