import re
import sys
set_list = []
for line in open(sys.argv[1]):
    line = re.sub(' +', ' ', line).strip()
    if '{' in line:
        set_list.append(line)
    if ';' in line:
        print('set', end=' ')
        for words in set_list:
            print(words.replace('{', ''), end='')
        print(line.replace(';', ''))
    if '}' in line:
        set_list.pop()