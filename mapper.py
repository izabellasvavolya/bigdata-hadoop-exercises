import sys, string
for line in sys.stdin:
    for w in line.strip().split():
        w = w.strip(string.punctuation).lower()
        if w:
            print(f"{w}\t1")
