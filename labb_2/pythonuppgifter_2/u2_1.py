### 2.1.1
def greeting(name):
    if name[0] == 'M':
        return 'Hej ' + name + ', visste du att M är min favoritbokstav!'
    return 'Hej ' + name + '!'

### 2.1.2
def is_this_a_long_list(values):
    return len(values) > 5

### 2.1.3
def get_grade(score):
    if score < 50:
        return 'U'
    elif 50 <= score <= 80:
        return 'G'
    elif score > 80:
        return 'VG'

### 2.1.4
def days_in_month(name_of_month):
    months = ['januari', 'februari', 'mars', 'april', 'maj', 'juni',' juli', 'augusti', 'oktober', 'november', 'december']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[months.index(name_of_month)]

### 2.1.5
def odd(value):
    return value % 2 == 1;

### 2.1.6
def get_integer_description(value):
    if value > 0 and not odd(value):
        return 2
    elif value > 0 and odd(value):
        return 1
    elif value == 0:
        return 0
    elif value < 0 and odd(value):
        return -1
    elif value < 0 and not odd(value):
        return -2

### 2.1.7
def appraisal_factor(rare, good_condition):
    factor = 1

    if rare:
        factor += 0.25
    else:
        factor -= 0.25
    
    if good_condition:
        factor += 0.5
    else:
        factor -= 0.5
    
    return factor