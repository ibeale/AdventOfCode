import sys

def get_input():
    input = []
    with open("input.txt") as f:
        input_list_str = f.read().split(',')
    for string in input_list_str:
        input.append(int(string))
    return input

def integer_to_array(num):
    arr = []
    string = str(num)
    for i in range(len(string)):
        arr.append(int(string[i]))
    return arr


def intCodeComp(input_list):
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
            input_list[input_list[i+1]] = int(input())
            i += 2
        elif operation == 4:
            p1 = input_list[i+1] if pmodes.pop() else input_list[input_list[i+1]]
            print(f"Printing value from position {input_list[i+1]}")
            print(p1)
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
            


    
        


def main():
    input = get_input()
    intCodeComp(input)


if __name__ == "__main__":
    main()