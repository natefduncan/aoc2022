def read_input(path: str):
    with open(path, "r") as f:
        output = f.read()
    return output

def parse_input(txt_block):
    keys = []
    data = {}
    for i in txt_block.split("\n"):
        if i.startswith("$ ls"):
            continue
        elif i.startswith("dir"):
            _, dir_name = i.split(" ")
            key = "".join(keys + [dir_name + "/"])
            data[key] = data.get(key, [])
        elif i.startswith("$ cd"):
            if ".." in i:
                keys.pop()
            else:
                keys.append(i.split(" ")[-1] + "/")
        else:
            if i:
                size, name = i.split(" ")
                key = "".join(keys)
                data[key] = data.get(key, []) + [(name, int(size))]
    return data

def folder_sizes(files): 
    output = {}
    for a in files.keys():
        total = 0
        for b in files.keys():
            if a in b:
                total += sum([x[1] for x in files[b]])
        output[a] = total
    return output

def p1():
    txt_block = read_input("input.txt")
    files = parse_input(txt_block)
    folders = folder_sizes(files)
    total = sum([v for v in folders.values() if v <= 100000])
    print(f"P1: {total}")

def p2():
    txt_block = read_input("input.txt")
    files = parse_input(txt_block)
    folders = folder_sizes(files)
    disk_size = 70000000
    min_disk_space = 30000000
    used_space = folders["//"]
    unused_space = disk_size - used_space
    to_delete = min_disk_space - unused_space
    delete_candidates = sorted([i for i in folders.values() if i >= to_delete])
    print(to_delete)
    print(f"P2: {delete_candidates[0]}")

if __name__=="__main__":
    p1()
    p2()
    # 3992669
    # 43992669
