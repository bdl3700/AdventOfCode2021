import sys
import numpy

if __name__ == '__main__':
    print('hello world')
    
    line = sys.stdin.readline().strip() # read in line 1 for length of counts array
    counts = [0 for i in range(len(str(line)))]

    def count_bits(line : str) -> None:
        line = str(line)
        for i in range(len(line)):
            if int(line[i]) > 0:
                counts[i] += 1
            else:
                counts[i] -= 1
    
    count_bits(line)  # count the bits in the first line

    for line in sys.stdin:
        line = line.strip()
        count_bits(line)  # count the remaining lines

    print(counts)

    # print gamma & epsilon
    gamma = numpy.uint32(0)
    epsilon = numpy.uint32(0)
    for j in range(len(line)):
        if counts[j] > 0:
            gamma += 2**(len(line)-j-1)
        else:
            epsilon += 2**(len(line)-j-1)


    print(gamma, epsilon, gamma * epsilon)
