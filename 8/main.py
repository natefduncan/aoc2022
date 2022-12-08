from typing import List, Tuple

Trees = List[List[int]]
Location = Tuple[int, int]
View = List[int]
Views = Tuple[View, View, View, View]

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_input(txt_block: str) -> Trees:
    return [[int(j) for j in list(i)] for i in txt_block.split("\n") if i]

def get_views(location: Location, trees: Trees) -> Views:
    row, col = location 
    left_locations = zip([row] * col, range(col))
    top_locations = zip(range(row), [col] * row)
    right_locations = zip([row] * (len(trees) - col), range(col + 1, len(trees)))
    bottom_locations = zip(range(row + 1, len(trees)), [col] * (len(trees) - row))
    return (
        [trees[r][c] for r, c in left_locations], 
        [trees[r][c] for r, c in top_locations], 
        [trees[r][c] for r, c in right_locations], 
        [trees[r][c] for r, c in bottom_locations], 
    )

def is_visible(height: int, views: Views) -> bool:
    left, top, right, bottom = views
    if not left or not top or not right or not bottom:
        return True
    return any([
        max(left) < height,
        max(top) < height, 
        max(right) < height, 
        max(bottom) < height
    ])

def distance(height: int, view: View) -> int:
    try:
        return [height > i for i in view].index(False) + 1
    except:
        return len(view)

def scenic_score(height: int, views: Views) -> int:
    left, top, right, bottom = views
    if not left or not top or not right or not bottom:
        return 0 
    dl = distance(height, left[::-1])
    dt = distance(height, top[::-1])
    dr = distance(height, right)
    db = distance(height, bottom)
    return dl * dt * dr * db

def p1():
    txt_block = read_input("input.txt")
    trees = parse_input(txt_block)
    total = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            height = trees[i][j]
            views = get_views((i, j), trees)
            visible = is_visible(height, views)
            total += 1 if visible else 0
    print(f"P1: {total}")

def p2():
    txt_block = read_input("input.txt")
    trees = parse_input(txt_block)
    scores = []
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            height = trees[i][j]
            views = get_views((i, j), trees)
            score = scenic_score(height, views)
            #  print(f"({i}, {j}) -> {score}")
            scores.append(score)
    print(f"P2: {max(scores)}")

if __name__=="__main__":
    p1()
    p2()


