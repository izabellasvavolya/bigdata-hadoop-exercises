from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator)
    results = []

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            results.append((current_word, total_count))
        except ValueError:
            pass


    results.sort(key=lambda x: x[1], reverse=True)

    for word, count in results[:3]:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
