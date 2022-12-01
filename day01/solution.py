def compare(current_max_elf, new_elf):
    return current_max_elf if new_elf <= current_max_elf else new_elf

def main():
    current_max = 0
    current_elf = 0

    for line in open("input.txt"):
        if line == "\n":
            current_max = compare(current_max, current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    
    current_max = compare(current_max, current_elf)

    print(current_max)

main()