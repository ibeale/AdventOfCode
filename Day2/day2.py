

def intCodeComp(inlist:int, first, second):

    input_list = []
    for i in inlist:
        input_list.append(i)

    input_list[1] = first
    input_list[2] = second
    
    for i in range(0, len(input_list), 4):
        if input_list[i] == 1:
            input_list[input_list[i+3]] = input_list[input_list[i+1]] + input_list[input_list[i+2]]
        elif input_list[i] == 2:
            input_list[input_list[i+3]] = input_list[input_list[i+1]] * input_list[input_list[i+2]]
        elif input_list[i] == 99:
            break
        else:
            print(f"Unknown opcode found: {input_list[i]} at location {i} Something went wrong.")
            return -1
    if input_list[0] == 19690720:
        return 1

def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split(',')

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])

    found = 0
    for i in range(100):
        for j in range(100):
            found = intCodeComp(input_list, i , j)
            if found == 1:
                print(f"Solution: i = {i}, j = {j}, 100*i+j = {100*i+j}")
                return
            if found == -1:
                print("No solution found")
                return


if __name__ == '__main__':
    main()