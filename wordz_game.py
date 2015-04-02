import copy


def is_word_in_table(word, table):
    is_word_here = False

    word = list(word)
    word_indx = 0

    table_copy = copy.deepcopy(table)

    row = len(table)
    col = len(table)

    for i in range(0, row):
        for j in range(0, col):
            if table[i][j] == word[word_indx]:
                if is_word_here is False:
                    word_copy = copy.deepcopy(word)
                    is_word_here = snake_word(
                        word_copy, table_copy, i, j, row, col, len(word), word_indx)
                    table_copy = copy.deepcopy(table)

    return is_word_here


def snake_word(word_copy, table_copy, x, y, row, col, word_len, word_indx):
    word_copy[word_indx] = '*'
    table_copy[x][y] = '*'

    # right
    if y + 1 < col and table_copy[x][y + 1] == word_copy[word_indx + 1]:
        snake_word(
            word_copy, table_copy, x, y + 1, row, col, word_len, word_indx + 1)

    # left
    if y - 1 >= 0 and table_copy[x][y - 1] == word_copy[word_indx + 1]:
        snake_word(
            word_copy, table_copy, x, y - 1, row, col, word_len, word_indx + 1)

    # up
    if x - 1 >= 0 and table_copy[x - 1][y] == word_copy[word_indx + 1]:
        snake_word(
            word_copy, table_copy, x - 1, y, row, col, word_len, word_indx + 1)

    # down
    if x + 1 < row and table_copy[x + 1][y] == word_copy[word_indx + 1]:
        snake_word(
            word_copy, table_copy, x + 1, y, row, col, word_len, word_indx + 1)

    # up - left
    if x - 1 >= 0 and y - 1 >= 0 and table_copy[x - 1][y - 1] == word_copy[word_indx + 1]:
        snake_word(word_copy, table_copy, x - 1, y - 1,
                   row, col, word_len, word_indx + 1)

    # uo - right
    if x - 1 >= 0 and y + 1 < col and table_copy[x - 1][y + 1] == word_copy[word_indx + 1]:
        snake_word(word_copy, table_copy, x - 1, y + 1,
                   row, col, word_len, word_indx + 1)

    # down - left
    if x + 1 < row and y - 1 >= 0 and table_copy[x + 1][y - 1] == word_copy[word_indx + 1]:
        snake_word(word_copy, table_copy, x + 1, y - 1,
                   row, col, word_len, word_indx + 1)

    # down - right
    if x + 1 < row and y + 1 < col and table_copy[x + 1][y + 1] == word_copy[word_indx + 1]:
        snake_word(word_copy, table_copy, x + 1, y + 1,
                   row, col, word_len, word_indx + 1)

    if word_copy[word_len - 2] == '*':
        return True
    else:
        return False


my_file = open("dictionary.txt", "r")

table = [['i', 'o', 't', 't'],
         ['e', 's', 'n', 'l'],
         ['p', 'x', 'n', 'g'],
         ['l', 'a', 'k', 'i']]

for row in range(0, 4):
    print (table[row])


if my_file:
    for line in my_file:
        if is_word_in_table(str(line), table) is True:
            print (line)
else:
    print ("Error!")
