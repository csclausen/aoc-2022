rpc_points = {
    "r": 1,
    "p": 2,
    "s": 3
}

rpc = {
    "X": "r",
    "Y": "p",
    "Z": "s",
    "A": "r",
    "B": "p",
    "C": "s"
}

def compare(opponents_move, my_move):
    if opponents_move == "r":
        if my_move == "p":
            return 6
        elif my_move == "r":
            return 3
    elif opponents_move == "p":
        if my_move == "s":
            return 6
        elif my_move == "p":
            return 3
    elif opponents_move == "s":
        if my_move == "r":
            return 6
        elif my_move == "s":
            return 3
    return 0

def round_total(opponents_move, my_move):
    return compare(opponents_move, my_move) + rpc_points[my_move]

def main():
    total = 0
    for line in open("input.txt"):
        moves = line.split()
        opponents_move = rpc[moves[0]]
        my_move = rpc[moves[1]]
        total += round_total(opponents_move, my_move)
    print(total)

main()