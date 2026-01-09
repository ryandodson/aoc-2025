# --- Day 1: Safe Dial ---
#
# Summary:
# - Algorithm: Circular/wrapping arithmetic using modulo
# - Data Structures: Simple iteration over lines, position tracking
# - Patterns: Modulo arithmetic for circular dial (0-99), string parsing
# - Math: Modular arithmetic for wrapping around dial positions
#
# Approach: Track dial position as rotations are applied, count how many times
# it points at 0. Part 2 counts zeros during rotations, not just at the end.


with open("day1input.txt", "r") as f:
    lines = f.read().splitlines()

current_position = 50
count_at_zero = 0

for rotation in lines:
    direction, distance = rotation[0], int(rotation[1:])
    current_position = (current_position + (distance if direction == 'R' else -distance)) % 100
    if current_position == 0:
        count_at_zero += 1

print(f"part 1: {count_at_zero}")


current_position = 50
zero_count = 0
prev_ended_at_zero = False

for line in lines:
    direction, distance = line[0], int(line[1:])
    start_pos = current_position
    
    step_delta = 1 if direction == 'R' else -1
    positions = [(start_pos + step * step_delta) % 100 for step in range(distance + 1)]
    
    zero_count += sum(
        1 for step, pos in enumerate(positions)
        if pos == 0 and not (step == 0 and prev_ended_at_zero)
    )
    
    current_position = positions[-1]
    prev_ended_at_zero = (current_position == 0)

print(f"part 2: {zero_count}")

