from math import floor


def integer_to_array(num):
    arr = []
    string = str(num)
    for i in range(len(string)):
        arr.append(int(string[i]))
    return arr


def is_increasing(digits):
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return 0
    return 1


def get_repeating(digits):
    repeating_nums = []
    for i in range(1, len(digits)):
        diff = digits[i] - digits[i-1]
        if diff == 0:
            repeating_nums.append(digits[i])
    return repeating_nums


def has_repeating(repeating_nums):
    if repeating_nums:
        for num in repeating_nums:
            if repeating_nums.count(num) == 1:
                return 1
        return 0
    else:
        return 0


def num_passwords():
    min = 231832
    max = 767346
    count = 0
    for i in range(min, max):
        num = i
        digits = integer_to_array(num)
        repeated = get_repeating(digits)
        if is_increasing(digits) and has_repeating(repeated):
            count += 1
    print(count)

def main():
    num_passwords()

if __name__ == "__main__":
    main()