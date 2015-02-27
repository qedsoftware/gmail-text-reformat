#!/usr/bin/env python
import fileinput
import sys

def format_lines(lines):
    n = len(lines)
    for i in xrange(0,n-1):
        cur = lines[i]
        nxt = lines[i+1]
        if not (cur.endswith('\n') and nxt.startswith('\n')):
            if cur == "\n":
                sys.stdout.write(cur.rstrip('\n'))
            else:
                sys.stdout.write(cur.rstrip('\n')+" ")
        else:
            sys.stdout.write(cur + "\n")
    sys.stdout.write(nxt)

def read_lines():
    with open(sys.argv[1],"r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please provide file to process as second argument.")
    lines = read_lines()
    format_lines(lines)
