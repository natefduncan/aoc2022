from typing import Tuple, List, Any, Optional

Coordinate = Tuple[int, int]
Path = Tuple[Coordinate, Coordinate]
Paths = List[Path]
Screen = List[List[Any]]

def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_coord(c: str) -> Coordinate:
    c1, c2 = c.split(",")
    return (int(c1), int(c2))

def parse_path(c1: str, c2: str) -> Path:
    p1 = parse_coord(c1)
    p2 = parse_coord(c2)
    return (p1, p2)

def parse_input(txt_block: str) -> Paths:
    paths = []
    for large_path in txt_block.split("\n"):
        small_paths = large_path.split(" -> ")
        for i in range(len(small_paths)-1):
            c1 = small_paths[i]
            c2 = small_paths[i+1]
            paths.append(parse_path(c1, c2))
    return paths

def get_coordinates(paths: Paths) -> List[Coordinate]:
    output = []
    for p in paths:
        c1, c2 = p
        output.append(c1)
        output.append(c2)
    return output

def find_bounds(paths: Paths) -> Tuple[int, int, int, int]:
    coords = get_coordinates(paths)
    min_y = 0
    max_y = max([i[1] for i in coords])
    min_x = min([i[0] for i in coords])
    max_x = max([i[0] for i in coords])
    return (min_x, min_y, max_x, max_y)

def expand_path(path: Path) -> List[Coordinate]:
    p1, p2 = path
    min_x = min([p1[0], p2[0]])
    max_x = max([p1[0], p2[0]])
    min_y = min([p1[1], p2[1]])
    max_y = max([p1[1], p2[1]])
    if min_x == max_x:
        return [(min_x, i) for i in range(min_y, max_y + 1)]
    elif min_y == max_y:
        return [(i, min_y) for i in range(min_x, max_x + 1)]
    else:
        return []

def debug(screen: Screen) -> str:
    output = ""
    for i, row in enumerate(screen):
        output += f"{i} " + "".join(row) + "\n"
    return output

def draw(paths: Paths) -> Screen:
    min_x, min_y, max_x, max_y = find_bounds(paths)
    rows = []
    for _ in range(max_y - min_y + 1):
        row = []
        for _ in range(max_x - min_x + 1):
            row.append(".")
        rows.append(row)
    for path in paths:
        coords = expand_path(path)
        for c in coords:
            x, y = c
            x = x - min_x
            y = y - min_y
            rows[y][x] = "#"
    return rows


def drop_sand(row: int, col: int, screen: Screen) -> Optional[Screen]:
    while True:
        try:
            screen[row][col]
            screen[row+1][col-1]
            screen[row+1][col+1]
        except:
            return None
        if screen[row+1][col] in ["o", "#"]:
            if screen[row+1][col-1] in ["o", "#"]:
                if screen[row+1][col+1] in ["o", "#"]:
                    if screen[row][col] in ["o", "#"]:
                        return None
                    else:
                        screen[row][col] = "o"
                        return screen
                else:
                    row += 1 
                    col += 1
            else:
                row += 1
                col -= 1
        else:
            row += 1
     
def p1():
    txt_block = read_input("input.txt")
    paths = parse_input(txt_block)
    min_x, _, _, _ = find_bounds(paths)
    screen = draw(paths)
    while True:
        x = drop_sand(0, 500 - min_x, screen)
        if not x:
            break
    total = len([i for j in screen for i in j if i == "o"])
    print(f"P1: {total}")

def p2():
    txt_block = read_input("input.txt")
    paths = parse_input(txt_block)
    _, _, _, max_y = find_bounds(paths)
    bottom_y = max_y + 2
    paths.append(((0, bottom_y), (1000, bottom_y)))
    min_x, _, _, _ = find_bounds(paths)
    screen = draw(paths)
    while True:
        x = drop_sand(0, 500 - min_x, screen)
        if not x:
            break
    total = len([i for j in screen for i in j if i == "o"])
    print(f"P2: {total}")


if __name__=="__main__":
    p1()
    p2()
