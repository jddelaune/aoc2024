# import dependencies
from pathlib import Path

# open the text file with the problem input and read into a string
p = Path('day4input.txt')
with p.open() as day4input:
    wordsearch = day4input.read()

# get a list of the horizontal lines in the word search puzzle
h_lines = wordsearch.splitlines()

# set up a list of empty strings for the vertical lines
v_lines = ['' for char in h_lines[0]]

# build a list of strings, one for each vertical line in the word search puzzle
for line in h_lines:
    for i, char in enumerate(line):
        v_lines[i] += char

# count up the number of times 'XMAS' or 'SAMX' is found in the horizontal & vertical lines
xmas_found = 0

for line in h_lines:
    xmas_found += line.count('XMAS')
    xmas_found += line.count('SAMX')

for line in v_lines:
    xmas_found += line.count('XMAS')
    xmas_found += line.count('SAMX')

# but, this doesn't count the diagnoals!

searches = {
            'l_to_r': [(1,0), (2,0), (3,0)],
            'r_to_l': [(-1,0), (-2,0), (-3,0)],
            'down': [(0,1),(0,2),(0,3)],
            'up': [(0,-1),(0,-2),(0,-4)],
            'up_r': [(1,-1),(2,-2),(3,-3)],
            'up_l': [(-1,-1),(-2,-2),(-3,-3)],
            'down_r': [(1,1),(2,2),(3,3)],
            'down_l': [(-1,1),(-2,2),(-3,3)]
            }

def find_word(a, b):
    """searches for 'XMAS' in all directions starting with the 'X' at coordinate a,b
    and returns the total number of 'XMAS'es found

    Args:
        a (int): horizontal coordinate
        b (int): vertical coordinate
    """    
# check if we are too close to left/right/bottom/top & should leave out those searches
# use the dictionary to see if the next letters 'M' 'A' 'S' are found in order. increment counter if so
# return counter




xmas_found = 0
v = 0

for line in h_lines:
    for h, char in enumerate(line):
    if char == 'X':
        words = find_word(h,v)
    v += 1