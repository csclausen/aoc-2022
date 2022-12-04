rpc_points = {
    "r": 1,
    "p": 2,
    "s": 3
}

rpc = {
    "A": "r",
    "B": "p",
    "C": "s"
}

x_mapping = {
    "r": "s",
    "p": "r",
    "s": "p"
}

z_mapping = {
    "r": "p",
    "p": "s",
    "s": "r"
}

def get_my_real_move(opponents_move, my_move):
    if my_move == "X":
        return x_mapping[opponents_move]
    elif my_move == "Y":
        return opponents_move
    else:
        return z_mapping[opponents_move]

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
    real_move = get_my_real_move(opponents_move, my_move)
    return compare(opponents_move, real_move) + rpc_points[real_move]

def main():
    total = 0
    for line in open("input.txt"):
        moves = line.split()
        opponents_move = rpc[moves[0]]
        my_move = moves[1]
        total += round_total(opponents_move, my_move)
    print(total)

main()