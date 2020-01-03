from itertools import permutations

class input_pair():
    def __init__(self, phase_setting):
        self.phase_setting = phase_setting
        self.input = None
        self.next_pair = None

    def get(self):
        if self.phase_setting != None:
            return_val = self.phase_setting
            self.phase_setting = None
            return return_val
        else:
            return self.input

    def set_input(self, input):
        self.input = input

    def set_next_pair(self, next_pair):
        self.next_pair = next_pair

    def __repr__(self):
        return self.phase_setting


def get_input():
    input = []
    #with open("input.txt") as f:
    #    input_list_str = f.read().split(',')
    input_list_str = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(',')
    for string in input_list_str:
        input.append(int(string))
    return input

def integer_to_array(num):
    arr = []
    string = str(num)
    for i in range(len(string)):
        arr.append(int(string[i]))
    return arr


def intCodeComp(input_list, pair):
    i = 0
    while(i<len(input_list)):
        arr = integer_to_array(input_list[i])
        instruction = [0] * 5
        for j in range(len(instruction) - 1, 0, -1):
            try:
                instruction[j] = arr.pop()
            except IndexError:
                break
        
        opcode = instruction[3:]
        pmodes = instruction[0:3]

        operation = opcode.pop()
        #print(f"Operation is {operation}")
        if operation == 1:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            p2 = input_list[i+2] if pmodes.pop() else input_list[input_list[i+2]]
            print(f"Placing {p1} + {p2} ({p1 + p2}) at location {input_list[i+3]}")
            input_list[input_list[i+3]] = p1 + p2
            i += 4
        elif operation == 2:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            p2 = input_list[i+2] if pmodes.pop() else input_list[input_list[i+2]]
            print(f"Placing {p1} * {p2} ({p1 * p2}) at location {input_list[i+3]}")
            input_list[input_list[i+3]] = p1 * p2
            i += 4
        elif operation == 3:
            print(f"Please input a number to place in position {input_list[i+1]}")
            input_list[input_list[i+1]] = pair.get()
            i += 2
        elif operation == 4:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            if pair.next_pair:
                pair.next_pair.set_input(p1)
            return p1
            #if (p1 != 0):
            #    print(f"Diagnostic error at {i}")
            i += 2
        elif operation == 5:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            p2 = input_list[i+2] if pmodes.pop() else input_list[input_list[i+2]]
            if p1 != 0:
                print(f"Setting instruction pointer to {p2}")
                i = p2
            else:
                i += 3
        elif operation == 6:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            p2 = input_list[i+2] if pmodes.pop() else input_list[input_list[i+2]]
            if p1 == 0:
                print(f"Setting instruction pointer to {p2}")
                i = p2
            else:
                i += 3
        elif operation == 7:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            p2 = input_list[i+2] if pmodes.pop() else input_list[input_list[i+2]]
            p3 = input_list[i+3]
            input_list[p3] = 1 if p1 < p2 else 0
            i += 4
        elif operation == 8:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            p2 = input_list[i+2] if pmodes.pop() else input_list[input_list[i+2]]
            p3 = input_list[i+3]
            input_list[p3] = 1 if p1 == p2 else 0
            i += 4
        elif operation == 9:
            if opcode.pop() == 9:
                return
        else:
            print(f"Unknown operator found {input_list[i]} at location {i}")
            return


def amplifier(input_pair_list):
    for pair in input_pair_list:
        input = get_input()
        val = intCodeComp(input, pair)
    return val

def main():
    phase_settings = [0,1,2,3,4]
    perm = permutations([0,1,2,3,4])
    maximum = 0
    for phase_settings in list(perm):
        input_pair_list = []
        for setting in phase_settings:
            input_pair_list.append(input_pair(setting))
        input_pair_list[0].set_input(0)
        for i in range(len(input_pair_list) - 1):
            input_pair_list[i].set_next_pair(input_pair_list[i+1])
        val = amplifier(input_pair_list)
        if val > maximum:
            maximum = val
            print(f"New maximum found {maximum}")
    print(maximum)
    
    #input = get_input()
    #intCodeComp(input)


if __name__ == '__main__':
    main()