from __future__ import print_function
import sys

def setsym(a, b):
    return len(set(a) ^ set(b))

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[:4]]
    print(setsym(lines[1], lines[3]))

if __name__ == '__main__':
    main()
