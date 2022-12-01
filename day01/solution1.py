def compare(current_max_elves, new_elf):
    current_max_elves.sort()
    if current_max_elves[0] < new_elf:
        current_max_elves[0] = new_elf
    
    return current_max_elves

def main():
    current_max_elves = [0, 0, 0]
    current_elf = 0

    for line in open("input.txt"):
        if line == "\n":
            current_max_elves = compare(current_max_elves, current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    
    current_max_elves = compare(current_max_elves, current_elf)

    print(sum(current_max_elves))

main()