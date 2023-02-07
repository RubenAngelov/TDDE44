# 3.1.1
def key_exists(key, d):
    return key in d

# 3.1.2
def value_exists1(value, d):
    return value in d.values()

# 3.1.3
def add_to_dict(key, value, d):
    d[key] = value

# 3.1.4
def add_new_only_to_dict(key, value, d):
    if key not in d:
        d[key] = value

# 3.1.5
def increment_dictionary_value1(key, d):
    d[key] += 1

# 3.1.6
def increment_dictionary_value2(key, d):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

# 3.1.7
def add_to_value_list1(key, value, d):
    d[key].append(value)

# 3.1.8
def return_value_list_1(prefix, d):
    values = []
    for key in d:
        if key[0:len(prefix)] == prefix:
            values.append(d[key])

    return values

# 3.1.9
def value_exists2(value, d):
    for key in d:
        if d[key] == value:
            return True
        elif type(d[key]) == list and value in d[key]:
            return True

    return False