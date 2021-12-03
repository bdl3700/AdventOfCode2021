import sys

if __name__ == '__main__':
    x = 0
    y = 0
    aim = 0
    for line in sys.stdin:
        line = line.split()
        dir = line[0][0]
        val = int(line[1])

        if dir == 'u':
            aim -= val
        elif dir == 'd':
            aim += val
        else:
            x += val
            y += aim * val

    print(x, y, (x * y))