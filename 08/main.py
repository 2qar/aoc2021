infile = "input"
entries = [[s.split() for s in line.split(" | ")] for line in open(infile).read()[0:-1].split("\n")]

def is_unique(out_str):
    return len(out_str) in [2, 3, 4, 7]

# Part 1
count = 0
for entry in entries:
    count += len(list(filter(is_unique, entry[1])))
print(count)

# Part 2
def add_possible_mappings(mapping, mappings, segment_choices):
    if len(segment_choices) == 0:
        mappings.append(mapping)
    else:
        for choice in segment_choices[0]:
            if choice not in mapping:
                add_possible_mappings(mapping + choice, mappings, segment_choices[1:])

def possible_mappings(segment_choices):
    mappings = []
    add_possible_mappings(str(segment_choices[0].pop()), mappings, segment_choices[1:])
    return mappings

def bitflags_to_int(flags):
    n = 0
    for i in flags:
        n |= 1 << i
    return n

# segments_to_num() convert a list of segment numbers to a number on a 7-segment
# display, where the indeces are as follows:
#
#     0000
#    1    2
#    1    2
#     3333
#    4    5
#    4    5
#     6666
#
# if the given segment numbers don't form a valid number, -1 is returned instead.
def segments_to_num(segment_nums):
    nums = [bitflags_to_int(idcs) for idcs in [
        [0,1,2,4,5,6],
        [2,5],
        [0,2,3,4,6],
        [0,2,3,5,6],
        [1,2,3,5],
        [0,1,3,5,6],
        [0,1,3,4,5,6],
        [0,2,5],
        [0,1,2,3,4,5,6],
        [0,1,2,3,5,6],
        ]]
    num = bitflags_to_int(segment_nums)
    try:
        return nums.index(num)
    except ValueError:
        return -1

def signals_to_numbers(signals_list, mapping):
    return list(map(lambda signals: segments_to_num(map(lambda c: mapping.index(c), signals)), signals_list))

def nums_to_num_aux(n, nums):
    if len(nums) == 0:
        return n
    else:
        return nums_to_num_aux(n * 10 + nums[0], nums[1:])

def nums_to_num(nums):
    return nums_to_num_aux(0, nums)

def decode_entry(entry):
    unique = list(filter(is_unique, entry[0]))
    unique.sort(key=lambda s: len(s))

    segments = []
    i = 0
    while i < 7:
        segments.append(set())
        i += 1
    unique_digit_segments = [
            [2, 5],  # 1
            [0],     # 7
            [1, 3],  # 4
            [4,6]]   # 8
    seen = {}
    for (signals, segment_nums) in zip(unique, unique_digit_segments):
        unseen_signals = list(filter(lambda c: c not in seen, signals))
        for i in segment_nums:
            for c in unseen_signals:
                segments[i].add(c)
        for c in unseen_signals:
            seen[c] = True

    for mapping in possible_mappings(segments):
        if sum(signals_to_numbers(entry[0], mapping)) == 45:
            return nums_to_num(signals_to_numbers(entry[1], mapping))

print(sum(map(decode_entry, entries)))
