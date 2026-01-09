# --- Day 7: Beam Splitting ---
#
# Summary:
# - Algorithm: State simulation, beam tracking
# - Data Structures: Sets for positions (part 1), defaultdict for counts (part 2)
# - Patterns: State machine simulation, set operations (update, add),
#   defaultdict for counting multiple timelines
# - Simulation: Track beam positions as they move down, split at '^' symbols
#
# Approach: Part 1 tracks beam positions as a set, counts splits. Part 2 uses
# defaultdict to count timelines at each position, handling quantum splitting.

with open("day7input.txt", "r") as f:
    lines = f.read().splitlines()

start_position = lines[0].index("S")
print("start_position: ", start_position)

def process_line(beam_positions, line, line_length):
    """Process a line and return (next_beam_positions, splits_count)."""
    next_positions = set()
    splits = 0
    
    for pos in beam_positions:
        if 0 <= pos < line_length:
            symbol = line[pos]
            if symbol == "^":
                next_positions.update(p for p in (pos - 1, pos + 1) if 0 <= p < line_length)
                splits += 1
            elif symbol in (".", "|"):
                next_positions.add(pos)
    
    return next_positions, splits

beam_positions = {start_position}
split_count = 0

for line_idx in range(1, len(lines)):
    beam_positions, splits_this_line = process_line(beam_positions, lines[line_idx], len(lines[line_idx]))
    split_count += splits_this_line

print("part 1: ", split_count)


from collections import defaultdict

def process_line_quantum(timeline_counts, line, line_length):
    next_counts = defaultdict(int)
    
    for pos, count in timeline_counts.items():
        if 0 <= pos < line_length:
            symbol = line[pos]
            if symbol == "^":
                if 0 <= pos - 1 < line_length:
                    next_counts[pos - 1] += count
                if 0 <= pos + 1 < line_length:
                    next_counts[pos + 1] += count
            elif symbol in (".", "|"):
                next_counts[pos] += count
    
    return next_counts

timeline_counts = {start_position: 1}

for line_idx in range(1, len(lines)):
    timeline_counts = process_line_quantum(timeline_counts, lines[line_idx], len(lines[line_idx]))

total_timelines = sum(timeline_counts.values())
print("part 2: ", total_timelines)

