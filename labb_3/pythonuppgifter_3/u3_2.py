# 3.2.1
def sum_of_ints2(value_list):
    s = 0
    for list in value_list:
        for value in list:
            if type(value) == int:
                s += value

    return s

# 3.2.2
def flatten_list1(list_of_lists):
    flattened = []
    for list in list_of_lists:
        flattened += list

    return flattened

# 3.2.3
def flatten_list2(list_of_lists):
    flattened = []
    for value in list_of_lists:
        if type(value) == list:
            flattened += value
        else:
            flattened.append(value)

    return flattened

# 3.2.4
def get_first_column(matrix):
    col = []
    for row in matrix:
        col.append(row[0])

    return col

# 3.2.5
def get_nth_column(n, matrix):
    col = []
    for row in matrix:
        col.append(row[n - 1])

    return col

# 3.2.6
def get_all_columns(matrix):
    columns = [[], [], []]
    for row in matrix:
        columns[0].append(row[0])
        columns[1].append(row[1])
        columns[2].append(row[2])

    return columns

m1 = [[1, 2, 4],
      [3, 0, 6],
      [0, 5, 1]]

# 3.2.7
def scalar_product(vec1, vec2):
    res = 0
    for e1, e2 in zip(vec1, vec2):
        res += e1 * e2

    return res

# 3.2.8
def matrix_square(matrix):
    squared = [[], [], []]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            jth_col = get_nth_column(j + 1, matrix)
            squared[i].append(scalar_product(matrix[i], jth_col))

    return squared

print(matrix_square(m1))