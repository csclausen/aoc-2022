def check_rucksacks(rucksacks_to_check):
    for c in rucksacks_to_check[0]:
        if c in rucksacks_to_check[1] and c in rucksacks_to_check[2]:
            return c

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
    step = 0
    with open("input.txt")as f:
        inputs = f.readlines()
        while step < len(inputs):
            rucksacks_to_check = inputs[step:step+3]
            duplicate = check_rucksacks(rucksacks_to_check)
            total += letter_score_mapping[duplicate]
            step += 3
    
    print(total)


main()