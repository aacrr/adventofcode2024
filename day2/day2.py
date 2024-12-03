def isValid(report):
    diff = []
    if len(report) == len(set(report)):
        for i in range(1, len(report)):
            diff.append(int(report[i]) - int(report[i-1]))
    if all(3 >= num >= 1 for num in diff) and len(diff) != 0:
        return True
    elif all(-3 <= num <= -1 for num in diff) and len(diff) != 0:
        return True

with open('day2.txt', 'r') as f:
    counter1 = 0
    counter2 = 0
    for line in f:
        report = line.split()
        if isValid(report):
            counter1 += 1
            counter2 += 1
        else:
            for i in range(len(report)):
                if isValid(report[:i]+report[i+1:]):
                    counter2 += 1
                    break

print(f'Part 1: {counter1}')
print(f'Part 2: {counter2}')
