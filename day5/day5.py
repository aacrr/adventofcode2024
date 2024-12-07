import re
from collections import defaultdict
from functools import cmp_to_key
page_orders = defaultdict(list)
s2 = False
counter = 0
counter2 = 0

def is_valid(find_num, page_orders) -> bool:
    find_num_rev = find_num[::-1]
    for page in find_num_rev:
        # 29, 53, 61, 47, 75
        check_num = page_orders[page]

        for num in check_num:
            if num in find_num_rev:
                if find_num_rev.index(page) < find_num_rev.index(num):
                    return False
    return True

# Part 2
def make_valid(find_num, page_orders):
    def compare(a, b):
        if a in page_orders[b]:
            return 1
        elif a not in page_orders[b]:
            return -1
        else:
            return 0

    find_num_rev = find_num[::-1]
    valid_pages = []
    for page in find_num_rev:
        check_num = page_orders[page]

        for num in check_num:
            if num in find_num_rev:
                if find_num_rev.index(page) < find_num_rev.index(num):
                    pass
                elif num not in valid_pages:
                    valid_pages.append(num)
    return sorted(find_num, key=cmp_to_key(compare))

with open('day5.txt', 'r') as f:
    for line in f:
        find_num = re.findall("\d+", line)
        if len(find_num) == 0:
            s2 = True
        elif not s2:
            if len(page_orders[find_num[0]]) == 0:
                page_orders[find_num[0]] = [find_num[1]]
            else:
                page_orders[find_num[0]].append(find_num[1])
        elif s2:
            if is_valid(find_num, page_orders):
                counter += int(find_num[(len(find_num)-1)//2])
            else:
                sorted_pages = make_valid(find_num, page_orders)
                counter2 += int(sorted_pages[(len(sorted_pages)-1)//2])

print(f'Part 1 : {counter}')
print(f'Part 2 : {counter2}')
