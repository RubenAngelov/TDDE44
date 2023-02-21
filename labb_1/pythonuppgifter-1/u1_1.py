### 1.1.1
def return_five():
    return 'five'

### 1.1.2
def print_five():
    print('five')

# print_five() returnerar standardvärdet 'None'.

### 1.1.3
def add_strings():
    return 'hej' + 'san'

# Det går att slå ihop fler strängar än två, och det paret av strängar längst till vänster slås ihop först.
# Att subtrahera strängar går däremot inte, och försöker man göra det får man ett felmeddelande som säger att den operationen ej är definerad för datatypen.

### 1.1.4
def use_the_var():
    value = 5
    return value * 5

# Det spelar inger roll vad variabeln är döpt till eftersom den existerar lokalt i funktionen. Finns det variabler med samma namn utanför funktionen gör det alltså ingenting.

### 1.1.5
def use_the_arg(a_string):
    print(a_string)
    return a_string

### 1.1.6
def to_string(a_value):
    return str(a_value)

### 1.1.7
def to_integer(a_value):
    return int(a_value)

### 1.1.8
def to_float(a_value):
    return float(a_value)

# Skillnaden mellan funktionerna är att de konverterar ett värde till olika datatyper.
# Ett flyttal har till skillnad från heltal en punkt och ett antal decimaler på slutet.
# När vi skriver to_float("exempel") får vi ett fellmeddelande som säger att en sträng inte går att konvertera till ett flyttal.

### 1.1.9
def to_any_type(a_value, a_type):
    return a_type(a_value)

### 1.1.10
def print_type(a_value):
    print(type(a_value))

### 1.1.11
def subtract(value1, value2):
    return value1, value2

# heltal - heltal resultater i heltal
# flyttal - flyttal resultater i flyttal
# heltal - flyttal resultater i flyttal
# flyttal - heltal resultater i flyttal

### 1.1.12
def split_bill(amount, number_of_people):
    amount_per_person = amount / number_of_people
    print(amount_per_person)
    return amount_per_person

### 1.1.13
import math

def round_up(value):
    return math.ceil(value)

### 1.1.14
import math

def round_down(value):
    return math.floor(value)

### 1.1.15
def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)

### 1.1.16
def celsius_to_fahrenheit(temperature):
    return temperature * (9 / 5) + 32

### 1.1.17
import math

def pythagoras(x, y):
    return math.sqrt((x * x) + (y * y))