import re

with open('day3.txt', 'r') as f:
    total1, total2 = 0, 0
    disabled = False
    for line in f:
        # Part 1
        for each in re.findall("mul\(\d{1,3},\d{1,3}\)", line):
            x = lambda a, b: int(a) * int(b)
            total1 += x(*re.findall("\d+", each))

        # Part 2
        for each in re.findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", line):
            cmd = ''.join(each)
            if cmd == "don't()":
                disabled = True
            elif cmd == "do()":
                disabled = False
            elif not disabled and re.findall("\d+", cmd):
                x = lambda a, b: int(a) * int(b)
                total2 += x(*re.findall("\d+", cmd))

print(f'Part 1 : {total1}')
print(f'Part 2 : {total2}')
