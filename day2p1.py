# import dependencies
from pathlib import Path

# open the text file with the problem input and read into a list
p = Path('day2input.txt')
with p.open() as day2input:
    raw_input = day2input.read()

# clean up the input:
    # remove newlines
input_lines = raw_input.splitlines()

# convert strings to integers and store reports in a list of lists
reports = []
for item in input_lines:
    txt_list = item.split(' ')
    num_set = []
    for txt in txt_list:
        num = int(txt)
        num_set.append(num)
    reports.append(num_set)

# define function to determine if a report is safe

def uniform_direction(report):
    """Return true if a report's values are all increasing or all decreasing.

    Args:
        report (list): a list of integers
    """

    checks = []
    values_count = len(report)
    
    # if any item is the same as the item before it, return False
    # build a list of checks, each one is true if the value is increasing and otherwise false
    for value_index in range(1, values_count):
        if report[value_index] == report[value_index - 1]:
            return False
        elif report[value_index] > report[value_index - 1]:
            checks.append(True)
        else:
            checks.append(False)
    
    # return true if all items in list are the same, otherwise return false
    if all(x == checks[0] for x in checks):
        return True
    return False

def within_tolerance(report):
    """Return true if the levels in a report differ by at least one and at most three.

    Args:
        report (list): a list of integers
    """
    values_count = len(report)
    for value_index in range(1, values_count):
        difference = abs(report[value_index] - report[value_index - 1])
        if difference >= 1 and difference <= 3:
            return True
    return False

def safety_check(report):
    """Return true if a report is safe. Both must be true for a report to be safe:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    Args:
        report (list): a list of integers
    """
    if uniform_direction(report) and within_tolerance(report):
        return True
    return False

safe_count = 0
for report in reports:
    if safety_check(report):
        safe_count += 1

print(safe_count)