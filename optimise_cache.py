#!/usr/bin/python
import sys

file_name = sys.argv[1]
with open(file_name) as f:
    line = f.readlines()[0]
new_lst = [l.split('.ansi-bold { font-weight: bold; } ')[2] if l.startswith('/* CSS font colors for translated ANSI escape sequences */') else l 
           for l in line.split('/*! * * IPython notebook * */ ')]
with open(file_name, 'w') as f:
    f.writelines(''.join(new_lst))

