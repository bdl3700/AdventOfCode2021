import sys

if __name__ == '__main__':
    prev = float('inf')
    result = 0
    for line in sys.stdin:
        line = int(line)
        if line > prev:
            result += 1
        prev = line
    print(result)