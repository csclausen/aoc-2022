def search_signal(signal, step):
    i = 0
    for x in range(0, len(signal)):
        if len(set(signal[i:i+step])) == step:
            return i+step
        i += 1

def main():
    with open("input.txt") as f:
        input_signal = f.read()
        print(f"Part 1 {search_signal(input_signal, 4)}")
        print(f"Part 2 {search_signal(input_signal, 14)}")



main()