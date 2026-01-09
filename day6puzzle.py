# --- Day 6: Vertical Equations ---
#
# Summary:
# - Algorithm: Column-wise parsing, string extraction
# - Data Structures: zip() for transposition, regex for number finding
# - Patterns: Transposing grid with zip(*rows), regex finditer for number positions,
#   column-wise digit extraction, right-to-left processing
# - String Operations: Regex matching, column indexing, digit extraction
#
# Approach: Part 1 reads equations horizontally (transpose with zip).
# Part 2 reads numbers vertically by extracting digits from columns, processing
# problems from right to left.

import re
from functools import reduce
from operator import mul

with open("day6input.txt", "r") as f:
    lines = f.read().splitlines()


cleaned_lines = [[word for word in line.split() if word] for line in lines]
equations = list(zip(*cleaned_lines))

part1_results = [eval(equation[-1].join(equation[:-1])) for equation in equations]
print("part 1: ", sum(part1_results))

max_width = max(len(line) for line in lines)
data_lines = lines[:-1]
operator_line = lines[-1]

operator_positions = [col for col in range(max_width) 
                      if col < len(operator_line) and operator_line[col] in '+*']

def get_digit_at_column(row_string, column_index):
    number_matches = [(match.start(), match.group()) 
                      for match in re.finditer(r'\d+', row_string)]
    
    for start_pos, number_string in reversed(number_matches):
        if start_pos <= column_index < start_pos + len(number_string):
            return number_string[column_index - start_pos]
    return None

def find_problem_column_range(operator_column):
    end_column = operator_column
    while (end_column < max_width - 1 and 
           any(end_column + 1 < len(line) and line[end_column + 1].strip() 
               for line in data_lines)):
        end_column += 1
    
    start_column = operator_column
    while (start_column > 0 and 
           any(start_column - 1 < len(line) and line[start_column - 1].strip() 
               for line in data_lines)):
        start_column -= 1
    
    return start_column, end_column

def extract_numbers_from_columns(start_column, end_column):
    numbers = []
    for column in range(end_column, start_column - 1, -1):
        digits = [digit for line in data_lines 
                  if (digit := get_digit_at_column(line, column)) is not None]
        if digits:
            numbers.append(int(''.join(digits)))
    return numbers[::-1]

part2_results = []
for operator_column in reversed(operator_positions):
    start_col, end_col = find_problem_column_range(operator_column)
    numbers = extract_numbers_from_columns(start_col, end_col)
    if numbers:
        operator = operator_line[operator_column]
        if operator == '+':
            result = sum(numbers)
        else:
            result = reduce(mul, numbers, 1)
        part2_results.append(result)

print("part 2: ", sum(part2_results))