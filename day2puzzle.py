# --- Day 2: Invalid Product IDs ---
#
# Summary:
# - Algorithm: String pattern matching (repeated digit patterns)
# - Data Structures: List comprehensions for filtering, range iteration
# - Patterns: Nested list comprehensions, string slicing and repetition checking
# - String Operations: Pattern detection by checking if number equals repeated substring
#
# Approach: Parse ID ranges, check each ID for repeated digit patterns (exactly 2x or at least 2x),
# sum all invalid IDs found across all ranges.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_repeated_pattern(n):
    str_n = str(n)
    for i in range(1, len(str_n) // 2 + 1):
        first_half = str_n[:i]
        second_half = str_n[i:]
        if second_half == first_half:
            return True
    return False

with open("day2input.txt", "r") as f:
    lines = f.read().split(",")
    
    invalid_ids = [
        i for line in lines
        for start, end in [[int(x) for x in line.split("-")]]
        for i in range(start, end + 1)
        if is_repeated_pattern(i)
    ]

invalid_id_sum = sum(invalid_ids)
print("part 1: ", invalid_id_sum)

def is_repeated_pattern_at_least_twice(n):
    str_n = str(n)
    for i in range(1, len(str_n) // 2 + 1):
        pattern = str_n[:i]
        if len(str_n) % len(pattern) == 0:
            num_repetitions = len(str_n) // len(pattern)
            if num_repetitions >= 2 and str_n == pattern * num_repetitions:
                return True
    return False

with open("day2input.txt", "r") as f:
    lines = f.read().split(",")
    
    invalid_ids = [
        i for line in lines
        for start, end in [[int(x) for x in line.split("-")]]
        for i in range(start, end + 1)
        if is_repeated_pattern_at_least_twice(i)
    ]

invalid_id_sum = sum(invalid_ids)
print("part 2: ", invalid_id_sum)