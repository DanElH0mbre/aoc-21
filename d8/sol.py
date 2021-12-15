def part1():
    f = open("input.txt", "r")
    unique_lengths = [2, 3, 4, 7]
    count = 0
    for l in f:
        o = l.strip().split(" | ")[1]
        sep = o.split(" ")
        for thing in sep:
            if len(thing) in unique_lengths:
                count += 1

def format(array):
    return "".join(sorted(array))

def get_uniques(key, i):
    for digit in i:
        if len(digit) == 2:
            key[1] = digit
        if len(digit) == 3:
            key[7] = digit
        if len(digit) == 4:
            key[4] = digit
        if len(digit) == 7:
            key[8] = digit

def get_6(key, i):
    for digit in i:
        if len(digit) == 6:
            count_in_1 = 0
            for char in digit:
                if char in key[1]:
                    count_in_1 += 1
            if count_in_1 == 1:
                key[6] = digit
                return
def get_9(key, i):
    for digit in i:
        if len(digit) == 6 and digit != key[6]:
            count_in_4 = 0
            for char in digit:
                if char in key[4]:
                    count_in_4 += 1
            if count_in_4 == 4:
                key[9] = digit
                return

def get_0(key, i):
    for digit in i:
        if len(digit) == 6 and digit != key[6] and digit != key[9]:
            key[0] = digit
            return

def get_3(key, i):
    for digit in i:
        if len(digit) == 5:
            count_in_7 = 0
            for char in key[7]:
                if char in digit:
                    count_in_7 += 1
            if count_in_7 == 3:
                key[3] = digit
                return

def get_5(key, i):
    for digit in i:
        if len(digit) == 5 and digit != key[3]:
            count_in_4 = 0
            for char in digit:
                if char in key[4]:
                    count_in_4 += 1
            if count_in_4 == 3:
                key[5] = digit

def get_2(key, i):
    for digit in i:
        if len(digit) == 5 and digit != key[3] and digit != key[5]:
            key[2] = digit
            return

def part2():
    f = open("input.txt", "r")
    total = 0
    for l in f:
        io = l.strip().split(" | ")
        i = [format(char) for char in io[0].split(" ")]
        o = [format(char) for char in io[1].split(" ")]
        key = {}
        get_uniques(key, i)
        get_6(key, i)
        get_9(key, i)
        get_0(key, i)
        get_3(key, i)
        get_5(key, i)
        get_2(key, i)
        flipped_key = {key[v] : v for v in key.keys()}
        c = 3
        real_output = 0
        for digit in o:
            real_output += flipped_key[digit] * 10 ** c
            c -= 1
        total += real_output
    print(total)

import time

s = time.perf_counter()

key = {}
part2()
print(time.perf_counter() - s)
