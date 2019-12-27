from math import floor

def main():
    input_list = []
    with open("input.txt", 'r') as input_file:
        for line in input_file.readlines():
            input_list.append(int(line))

    sum = 0

    for input in input_list:
        sum += floor(input / 3) - 2
    
    print(f"Sum = {sum}")


if __name__ == "__main__":
    main()