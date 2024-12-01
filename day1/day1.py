import re
from collections import Counter

def part1(left, right):
    # Loop through lists again to calculate total distance
    total_distance = 0
    for num1, num2 in zip(left, right):
        total_distance += abs(num1 - num2)
    return total_distance

def part2(left, count_right):
    sim_score = 0
    # Calculate similarity score
    for i in left:
        sim_score += i * count_right[i]
    return sim_score

left, right = [], []
with open('day1.txt', 'r') as f:
    for line in f:
        # Used regex to find the numbers
        nums = re.findall("\d+", line)
        left.append(int(nums[0]))
        right.append(int(nums[1]))

left.sort()
right.sort()
count_right = Counter(right)

print(f'Part 1: {part1(left, right)}')
print(f'Part 2: {part2(left, count_right)}')
