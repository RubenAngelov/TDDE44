# 2.2.1
def create_ten_list_while():
    new_list = []
    i = 0
    while i <= 10:
        new_list.append(i)
        i += 1

    return new_list

def create_ten_list_for():
    new_list = []
    for i in range(11):
        new_list.append(i)
    
    return new_list

# 2.2.2
def create_zero_to_number_list_while(number):
    new_list = []
    i = 0
    while i <= number:
        new_list.append(i)
        i += 1

    return new_list

def create_zero_to_number_list_for(number):
    new_list = []
    for i in range(number + 1):
        new_list.append(i)

    return new_list

# 2.2.3
def create_number_to_number_list_while(start_number, end_number):
    new_list = []
    i = start_number
    while i <= end_number:
        new_list.append(i)
        i += 1

    return new_list

def create_number_to_number_list_for(start_number, end_number):
    new_list = []
    for i in range(start_number, end_number + 1):
        new_list.append(i)

    return new_list

# 2.2.4
def get_max_while(integer_list):
    max_value = -1
    i = 0
    while i < len(integer_list):
        if integer_list[i] > max_value:
            max_value = integer_list[i]
        i += 1

    return max_value

def get_max_for(integer_list):
    max_value = -1
    for value in integer_list:
        if value > max_value:
            max_value = value

    return max_value

# 2.2.5
def get_min(integer_list):
    min_value = -1
    for value in integer_list:
        if value < min_value or min_value == -1:
            min_value = value

    return min_value

# 2.2.6
def word_in_list_while(words, word):
    i = 0
    while i < len(words):
        if words[i] == word:
            return True
        i += 1

    return False

def word_in_list_for(words, word):
    for candidate in words:
        if candidate == word:
            return True

    return False

# 2.2.7
def count_integers_while(value_list):
    num_integers = 0
    i = 0
    while i < len(value_list):
        if type(value_list[i]) == int:
            num_integers += 1
        i += 1        

    return num_integers

def count_integers_for(value_list):
    num_integers = 0
    for value in value_list:
        if type(value) == int:
            num_integers += 1

    return num_integers

# 2.2.8
def average_while(values):
    sum_of_values = 0
    i = 0
    while i < len(values):
        sum_of_values += values[i]
        i += 1

    return sum_of_values / len(values)

def average_for(values):
    sum_of_values = 0
    for value in values:
        sum_of_values += value

    return sum_of_values / len(values)

# 2.2.9
def population(pop_a, rate_a, pop_b, rate_b):
    if rate_b > rate_a:
        return -1

    years_taken = 0
    while pop_a < pop_b:
        pop_a *= 1 + rate_a / 100
        pop_b *= 1 + rate_b / 100
        years_taken += 1

    return years_taken

def population_2(pop_a, rate_a, pop_b, rate_b):
    # Se till att 'a' alltid har den minsta ursprungliga befolkningen.
    if pop_b < pop_a:
        pop_a, pop_b = pop_b, pop_a
        rate_a, rate_b = rate_b, rate_a

    if rate_b > rate_a:
        return -1

    years_taken = 0
    while pop_a < pop_b:
        pop_a *= 1 + rate_a / 100
        pop_b *= 1 + rate_b / 100
        years_taken += 1

    return years_taken

# 2.2.10
def birthday(n):
    second_term = 1
    for i in range(1, n + 1):
        second_term *= (366 - i) / 365

    return 1 - second_term

# 2.2.11
def sum_of_ints(value_list):
    s = 0
    for value in value_list:
        if type(value) == int:
            s += value

    return s

