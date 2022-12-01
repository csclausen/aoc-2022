with open("input.txt") as f:
    print(max(sum(int(x) if x else 0 for x in y.split("\n")) for y in f.read().split("\n\n")))