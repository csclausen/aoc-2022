def get_elf_range(elf_zones):
    # looks like 2-4
    elf_range = elf_zones.split("-")
    return elf_range[0], elf_range[1]

def split_elf_ranges(input_line):
    # looks like 2-4,6-8
    elves = input_line.split(",")
    return elves[0], elves[1]

def ranges_intersect(e1_range, e2_range):
    return elf_range_inside(e1_range, e2_range) or elf_range_inside(e2_range, e1_range)

def elf_range_inside(e1_range, e2_range):
    return int(e1_range[0]) <= int(e2_range[0]) and int(e1_range[1]) >= int(e2_range[1])
        

def main():
    pairs = 0
    import pdb
    for line in open("input.txt"):
        elf1, elf2 = split_elf_ranges(line)
        e1_range = get_elf_range(elf1)
        e2_range = get_elf_range(elf2)
        if ranges_intersect(e1_range, e2_range):
            pairs += 1
    
    print(pairs)
        


main()