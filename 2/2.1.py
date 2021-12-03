import sys

if __name__ == '__main__':
    x, y = 0, 0
    for line in sys.stdin:
        line = line.split()
        dir = line[0][0]
        val = int(line[1])

        if dir == 'u':
            y -= val
        elif dir == 'd':
            y += val
        else:
            x += val

    print(x, y, (x * y))
