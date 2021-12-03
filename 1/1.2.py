import sys
from typing import List

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        line = int(line)
        lines.append(line)

    result = 0
    prev = float('inf')
    for i in range(1, len(lines) - 1):
        val = lines[i - 1] + lines[i] + lines[i + 1]
        if val > prev:
            result += 1
        prev = val

    print(result)