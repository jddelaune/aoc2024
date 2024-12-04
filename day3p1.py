# import dependencies
from pathlib import Path
import re

# open the text file with the problem input and read into a string
p = Path('day3input.txt')
with p.open() as day3input:
    corrupted = day3input.read()

# set up total variable
total = 0

# find all matches
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', corrupted)

# multiply each match pair and add to total
for m in matches:
    mul = int(m[0]) * int(m[1])
    total = total + mul

# print the total
print(total)