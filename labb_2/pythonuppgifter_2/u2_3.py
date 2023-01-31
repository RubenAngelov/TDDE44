# 2.3.1
def replace_periods_with_newlines(string_value):
    ret_string = ''
    for char in string_value:
        if char == '.':
            ret_string += '\n'
        else:
            ret_string += char

    return ret_string

# 2.3.2
def replace_char_in_string(original_string, search_character, replacement):
    ret_string = ''
    for char in original_string:
        if char == search_character:
            ret_string += replacement
        else:
            ret_string += char

    return ret_string

# 2.3.3
def reverse_string_while(string_value):
    reversed = ''
    i = len(string_value) - 1
    while i >= 0:
        reversed += string_value[i]
        i -= 1
    
    return reversed

def reverse_string_for(string_value):
    reversed = ''
    for i in range(len(string_value) - 1, -1, -1):
        reversed += string_value[i]

    return reversed

# 2.3.4
def get_five_first(value_list):
    first_five = []
    for i in range(5):
        first_five.append(value_list[i])

    return first_five

# 2.3.5
def get_nfirst(value_list, n):
    first_n = []
    for i in range(n):
        first_n.append(value_list[i])

    return first_n

# 2.3.6
def get_all_less_than(values, cutoff):
    values_less_than = []
    for value in values:
        if value < cutoff:
            values_less_than.append(value)

    return values_less_than

# 2.3.7
def get_all_even(values):
    even_values = []
    for value in values:
        if value % 2 == 0:
            even_values.append(value)

    return even_values

# 2.3.8
def get_all_divisible(values, divisor):
    divisible_values = []
    for value in values:
        if value % divisor == 0:
            divisible_values.append(value)

    return divisible_values

# 2.3.9
def multiply_for_each(values, multiplier):
    for i in range(len(values)):
        values[i] *= multiplier

    return values

# 2.3.10
def insert_at_asc_place(values, new_value):
    # Hantera tom input-lista
    if not values: 
        return [new_value]

    low = 0
    high = len(values) - 1
    # Halvera delen av listan vi tittar på tills bara ett listelement är kvar.
    while low != high:
        mid = int((low + high) / 2)
        if (new_value < values[mid]):
            high = mid - 1
        elif (new_value > values[mid]):
            low = mid + 1
    
    # Lägg in new_value antingen framför eller efter detta listelement.
    mid = int((low + high) / 2)
    if (new_value < values[mid]):
        values.insert(mid, new_value)
    else:
        values.append(new_value)

    return values

# 2.3.11
def sort_asc(values):
    sorted_values = []
    for value in values:
        sorted_values = insert_at_asc_place(sorted_values, value)

    return sorted_values