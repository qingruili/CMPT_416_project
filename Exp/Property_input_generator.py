from faker import Faker
import random
import string
from Random_strings_Property import *
fake = Faker()

#global values used as a default range for generating random data
min_int = -1000
max_int = 1000

min_flt = -1000.0
max_flt = 1000.0

# functions for generating random data

def random_int():
    return fake.random_int(min_int, max_int)

def random_float():
    return fake.pyfloat(None, None, False,  min_flt, max_flt)


# returns a list of n test cases for the given function "f_correct"
def test_cases_maker_property(f_correct, arg_types):
    input_cases = []
    str_generator_functions = [random_str, random_word, random_lowercase_string, random_uppercase_string, empty_string]
    for i in range(5):
        case = []
        for type in arg_types:
            if type == 'int':
                case.append(random_int())
            elif type == 'str':
                case.append(str_generator_functions[i%5](10))
            elif type == "list":
                case.append([random.randint(1, 100) for _ in range(10)])
        input_cases.append(case)
    return input_cases
