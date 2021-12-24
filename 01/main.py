nums = [int(x) for x in open("input", "r").read().split('\n')[0:-1]]

# Part 1
pairs = []
i = 0
while i < len(nums) - 1:
    pairs.append((nums[i], nums[i+1]))
    i += 1
print(len(list(filter(lambda p: p[0] < p[1], pairs))))

# Part 2
windows = []
i = 0
while i < len(nums) - 2:
    windows.append(nums[i] + nums[i+1] + nums[i+2])
    i += 1
pairs = []
i = 0
while i < len(windows) - 1:
    pairs.append((windows[i], windows[i+1]))
    i += 1
print(len(list(filter(lambda p: p[0] < p[1], pairs))))
