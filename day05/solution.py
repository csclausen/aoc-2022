import queue

def parse_box_structure(input_array):
    lifo_queues = dict()
    step = 4
    for line in reversed(input_array[0:8]):
        for i in range(1, len(line), step):
            if line[i].strip():
                if i not in lifo_queues:
                    lifo_queues[i] = queue.LifoQueue()
                lifo_queues[i].put(line[i])

    # transform so the keys are 1-9
    keys = list(lifo_queues.keys())
    mapped_lifo_queues = dict()
    for i in range(1, len(keys) + 1):
        mapped_lifo_queues[i] = lifo_queues[keys[i-1]]

    return mapped_lifo_queues

def move_boxes(stacks, num_to_move, start_stack, dest_stack):
    for i in range(0, num_to_move):
        if stacks[start_stack].empty():
            return stacks
        stacks[dest_stack].put(stacks[start_stack].get())
    
    return stacks

def parse_move(line):
    parsed_move = [int(x) for x in line.split(" ") if x.isdigit()]
    
    return parsed_move

def get_tops(stacks):
    stack_string = ""
    for i in stacks:
        stack_string = stack_string + stacks[i].get()
    
    return stack_string

def main():
    with open("input.txt") as f:
        inputs = f.readlines()
        stacks = parse_box_structure(inputs)
        # lazy
        moves = inputs[10:]
        for line in moves:
            move = parse_move(line.strip())
            stacks = move_boxes(stacks, move[0], move[1], move[2])
        
        print(get_tops(stacks))
        

main()