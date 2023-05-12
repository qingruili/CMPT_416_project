
from faker import Faker
import random
import string
import inspect


fake = Faker()

#global values used as a default range for generating random data
min_int = -1000
max_int = 1000

min_flt = -1000.0
max_flt = 1000.0

# returns the argument types from a function
# arg_list = ['int', 'int', 'str']
def argType_parser(fn):
    signature = str(inspect.signature(fn))
    arg_list = signature[1:-1].split(',')
    for i, s in enumerate(arg_list): arg_list[i] = s[s.find(':')+2:]
    return arg_list

# functions for generating random data
def random_letter():
    return random.choice(string.ascii_letters)

def random_digit():
    return random.choice(string.digits)

def random_punctuation():
    return random.choice(string.punctuation)

def random_whitespace():
    return random.choice(string.whitespace)

def random_char():
    return random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')

def random_str(length):
    return ''.join(random_char() for _ in range(length))

def random_int():
    return fake.random_int(min_int, max_int)

def random_float():
    return fake.pyfloat(None, None, False,  min_flt, max_flt)


# returns a list of n test cases for the given function "f_correct"
def test_cases_maker(f_correct, n):
    input_cases = []
    arg_types = argType_parser(f_correct)
    for i in range(n):
        case = []
        for type in arg_types:
            if type == 'int':
                case.append(random_int())
            elif type == 'str':
                length = random.randint(1, 10)
                case.append(random_str(length))
        input_cases.append(case)

    return input_cases



# returns a dictionary containing the data for testing the function
def test_dict_maker(f_correct, length):
    arg_types = argType_parser(f_correct) # arg_types = ['int', 'int', 'str']
    return {"input_cases": test_cases_maker(f_correct, length ),
            "correct_function": f_correct,
            "arity": len(arg_types),
            "argument_types": arg_types, 
            "name": 'sample_test_case_maker',
            "note": 'just for testing',
           }

# given a dictionary containing material and data for testing a function "f_student", run all tests.
def run_tests(f_student, test_case_dict):
    input_cases = test_case_dict['input_cases']
    correct_function = test_case_dict['correct_function']
    name = test_case_dict['name']
    flag = True
    for input_case in input_cases:
        if f_student(*input_case) != correct_function(*input_case):
            print('FAIL: ' + name + '(' + str(input_case) + ')')
            print('     returned: ' + str(f_student(*input_case)))
            print('     expected: ' + str(correct_function(*input_case)))
            flag = False
    return flag

