# --- Day 5: Fresh Ingredients ---
#
# Summary:
# - Algorithm: Range merging, set membership checking
# - Data Structures: Sets, list comprehensions, tuples for ranges
# - Patterns: Range merging (sort and merge overlapping/adjacent ranges),
#   set comprehension with any() for membership testing
# - Math: Sum of range lengths (end - start + 1)
#
# Approach: Part 1 finds ingredients in any range using set comprehension.
# Part 2 merges overlapping ranges and sums total unique numbers across all ranges.

with open("day5input.txt", "r") as f:
    lines = f.read().splitlines()
    
    empty_line_idx = next(i for i, line in enumerate(lines) if line == "")
    ranges = lines[:empty_line_idx]
    ingredients = [int(line) for line in lines[empty_line_idx + 1:] if line.strip()]

parsed_ranges = [
    (int(start), int(end))
    for line in ranges
    for start, end in [line.split("-")]
]

fresh = {
    ingredient for ingredient in ingredients
    if any(start <= ingredient <= end for start, end in parsed_ranges)
}

print("part 1: ", len(fresh))

sorted_ranges = sorted(parsed_ranges, key=lambda x: x[0])

merged = []
for start, end in sorted_ranges:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

total_fresh = sum(end - start + 1 for start, end in merged)
print("part 2: ", total_fresh)