from collections import deque
import os

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

with open('mock_file.txt', 'r') as f:
    for line, prevlines in search(f, 'Python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)

