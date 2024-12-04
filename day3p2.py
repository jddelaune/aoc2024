# import dependencies
from pathlib import Path
import re

# open the text file with the problem input and read into a string
p = Path('day3input.txt')
with p.open() as day3input:
    corrupted = day3input.read()

# get an iterable with each proper mul() group, do(), and don't()
matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', corrupted)

# set variables, do is true because the multiplication is enabled at the start of the string
do = True
total = 0

# iterate through matches, enable multiplication on 'do' and disable it on 'don't' and multiply
# then add if it is a mul() group and multiplication is enabled
for m in matches:
    result = m.group(0)
    match result:
        case "do()":
            do = True
        case "don't()":
            do = False
        case _ if do:
            total += int(m.group(1)) * int(m.group(2))

print(total)
