# --- Day 3: Battery Banks ---
#
# Summary:
# - Algorithm: Greedy algorithm for digit selection
# - Data Structures: String manipulation, list comprehensions
# - Patterns: Greedy selection (choose largest available digit while ensuring enough remain),
#   itertools.combinations for part 1 (selecting 2 digits)
# - String Operations: Concatenation, digit extraction
#
# Approach: Part 1 uses combinations to find max 2-digit number. Part 2 uses greedy
# algorithm: at each position, select largest digit available while leaving enough
# digits to complete the 12-digit number.

def find_largest_joltage(line):
    return max(
        int(line[i] + line[j])
        for i in range(len(line))
        for j in range(i + 1, len(line))
    )

def find_total_output_joltage(lines):
    return sum(find_largest_joltage(line) for line in lines)

with open("day3input.txt", "r") as f:
    lines = f.read().splitlines()
    print("part 1: ", find_total_output_joltage(lines))

def find_largest_twelve_digit_number(line):
    n = len(line)
    k = 12
    result = []
    start_idx = 0
    
    for position in range(k):
        end_idx = n - (k - position)
        
        max_digit = '0'
        max_idx = start_idx
        for i in range(start_idx, end_idx + 1):
            if line[i] > max_digit:
                max_digit = line[i]
                max_idx = i
        
        result.append(max_digit)
        start_idx = max_idx + 1
    
    return int(''.join(result))

def total_output(lines):
    return sum(find_largest_twelve_digit_number(line) for line in lines)

with open("day3input.txt", "r") as f:
    lines = f.read().splitlines()
    print("part 2: ", total_output(lines))