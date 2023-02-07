# 3.3.1
def fac_rec(n):
    if n == 1:
        return 1
    else:
        return n * fac_rec(n - 1)

# 3.3.2
def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# 3.3.3
def pascal(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col - 1) + pascal(row - 1, col)

# 3.3.4
def keep_if_even(lst):
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            return keep_if_even(lst[0:i] + lst[i+1:])

    return lst

# 3.3.5
def reverse_rec(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_rec(lst[:-1])

# 3.3.6
def keep_if_even_all(lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = keep_if_even_all(lst[i])
        elif type(lst[i]) == int and lst[i] % 2 != 0:
            return keep_if_even_all(lst[0:i] + lst[i+1:])

    return lst

# 3.3.7
def reverse_rec_all(lst):
    if len(lst) == 0: 
        return []
    elif type(lst[-1]) == list:
        lst[-1] = reverse_rec_all(lst[-1])
    
    return [lst[-1]] + reverse_rec_all(lst[:-1])

# 3.3.8
def is_in_list(lst, element):
    if not lst:
        return False
    elif type(lst[0]) == list and is_in_list(lst[0], element):
        return True
    elif lst[0] == element:
        return True
    else:
        return is_in_list(lst[1:], element)

# 3.3.9
def count_all(lst):
    if not lst:
        return 0
    elif type(lst[0]) == list: 
        return count_all(lst[1:]) + count_all(lst[0])
    else:
        return count_all(lst[1:]) + 1

# 3.3.10
def subst_all(lst, element, new_value):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = subst_all(lst[i], element, new_value)
        else:
            if lst[i] == element:
                lst[i] = new_value

    return lst

# 3.3.11
def multiply(factor1, factor2):
    if factor2 == 1:
        return factor1
    else:
        return factor1 + multiply(factor1, factor2 - 1)