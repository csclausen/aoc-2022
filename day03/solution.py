def split(input_line):
    mid = len(input_line) // 2
    return input_line[0:mid], input_line[mid:]

def find_duplicate(s1, s2):
    for c in s1:
        if c in s2:
            return c

def create_alphabet_mapping():
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_score_mapping = dict()
    i = 1
    for letter in letters:
        letter_score_mapping[letter] = i
        letter_score_mapping[letter.upper()] = i + 26
        i += 1
    return letter_score_mapping


def main():
    letter_score_mapping = create_alphabet_mapping()
    total = 0
    for line in open("input.txt"):
        s1, s2 = split(line)
        duplicate = find_duplicate(s1, s2)
        total += letter_score_mapping[duplicate]
    
    print(total)


main()