with open('day4.txt', 'r') as f:
    counter = 0
    total_lines = f.readlines()
    search_word = 'XMAS'
    search_word2 = 'MAS'
    counter2 = 0

    words = list(map(str.strip, total_lines))
    for row in words:
        for index_char, char in enumerate(row):
            index_row = words.index(row)
            # Part 2

            # Checking bounds for ddr and then ddl
            if index_row+len(search_word2) <= len(words) and index_char+len(search_word2) <= len(row):
                search_ddr = [total_lines[index_row + i][index_char + i] for i in range(len(search_word2))]
                search_ddl = [total_lines[index_row + i][index_char + len(search_word2) - 1 - i] for i in range(len(search_word2))]
                if (''.join(search_ddr) == search_word2 and ''.join(search_ddl) == search_word2[::-1]) or (''.join(search_ddr) == search_word2[::-1] and ''.join(search_ddl) == search_word2) or (''.join(search_ddr) == search_word2 and ''.join(search_ddl) == search_word2) or (''.join(search_ddr) == search_word2[::-1] and ''.join(search_ddl) == search_word2[::-1]):
                    counter2 += 1

            # Part 1
            if char == search_word[0]:
                # Searching right
                if index_char+len(search_word) <= len(row):
                    search_r = ''.join([total_lines[index_row][index_char+i] for i in range(len(search_word))])
                    if search_r == search_word:
                        counter += 1

                # Searching left
                if index_char-len(search_word)+1 >= 0:
                    search_l = ''.join([total_lines[index_row][index_char - i] for i in range(len(search_word))])
                    if search_l == search_word:
                        counter += 1

                # Searching downwards
                if index_row+len(search_word) <= len(words):
                    search_d = [total_lines[i][index_char] for i in range(index_row, index_row+len(search_word))]
                    if ''.join(search_d) == search_word:
                        counter += 1

                # Searching upwards
                search_u = [total_lines[i][index_char] for i in range(index_row, index_row - len(search_word), -1)]
                if index_row-len(search_word)+1 >= 0 and ''.join(search_u) == search_word:
                    counter += 1

                # Searching diagonally upwards to the right (dur)
                if index_row-len(search_word)+1 >= 0 and index_char+len(search_word) <= len(row):
                    search_dur = [total_lines[index_row-i][index_char+i] for i in range(len(search_word))]
                    if ''.join(search_dur) == search_word:
                        counter += 1

                # Searching diagonally upwards to left (dul)
                if index_row-len(search_word)+1 >= 0 and index_char-len(search_word)+1 >= 0:
                    search_dul = [total_lines[index_row-i][index_char-i] for i in range(len(search_word))]
                    if ''.join(search_dul) == search_word:
                        counter += 1

                # Searching diagonally downwards to right (ddr)
                if index_row+len(search_word) <= len(words) and index_char+len(search_word) <= len(row):
                    search_ddr = [total_lines[index_row+i][index_char+i] for i in range(len(search_word))]
                    if ''.join(search_ddr) == search_word:
                        counter += 1

                # Searching diagonally downwards to left (ddl)
                if index_row+len(search_word) <= len(words) and index_char-len(search_word)+1 >= 0:
                    search_ddl = [total_lines[index_row+i][index_char-i] for i in range(len(search_word))]
                    if ''.join(search_ddl) == search_word:
                        counter += 1

print(f'Part 1 : {counter}')
print(f'Part 2 : {counter2}')
