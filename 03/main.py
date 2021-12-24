nums = open("input").read().split('\n')[0:-1]
columns = len(nums[0])

def bit_for_col(ns, i, m, stalemate_value):
    zeroes = len(list(filter(lambda x: x == '0', [n[i] for n in ns])))
    ones = len(list(filter(lambda x: x == '1', [n[i] for n in ns])))
    if ones == zeroes:
        return stalemate_value
    else:
        return m if ones > zeroes else not m

def mcb(ns, i):
    return bit_for_col(ns, i, True, 1)

def lcb(ns, i):
    return bit_for_col(ns, i, False, 0)

def bits(f):
    bits = []
    for i in range(columns):
        bits.append(f(nums, i))
    return bits

def bin_to_dec(bits_array):
    a = bits_array[::-1]
    i = 0
    n = 0
    while i < len(bits_array):
        n += 2**i * a[i]
        i += 1
    return n

# Part 1
print(bin_to_dec(bits(mcb)) * bin_to_dec(bits(lcb)))

# Part 2
def bits_criteria(m, stalemate_value):
    o = nums
    i = 0
    while len(o) > 1:
        mc = bit_for_col(o, i, m, stalemate_value)
        o = list(filter(lambda n: n[i] == chr(mc + 0x30), o))
        i += 1
    return [int(x) for x in o[0]]

print(bin_to_dec(bits_criteria(True, 1)) * bin_to_dec(bits_criteria(False, 0)))
