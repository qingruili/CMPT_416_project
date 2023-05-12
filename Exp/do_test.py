from test import *
from import_file import *
import sys
from extract_path import *
from Tester import *
from Property_input_generator import *


num_random_test = sys.argv[2]


if __name__ == '__main__':
    question_folder_path = paths(sys.argv[1])
    question_function = sys.argv[1]

    new_files = import_file(question_folder_path,question_function)
    test_cases_property = f'test_cases_maker_property({new_files[0]}.{question_function}, argType_parser({new_files[0]}.{question_function}))'
    test_cases = eval(test_cases_property)

    lis= []

    for i in range(len(new_files)-1):
        input_generate=f'input_generator({new_files[0]}.{question_function},{new_files[i+1]}.{question_function},{test_cases},{new_files[i+1]})'
        htl= eval(input_generate)
        lis.append(htl)
    
    
    append_rts=f'append_random_test({new_files[0]}.{question_function},{num_random_test})'
    eval(append_rts)
    for i in range(len(new_files)-1):
        
        run_dotests =f'run_doctest({new_files[0]}.{question_function},{new_files[i+1]}.{question_function},{new_files[i+1]},lis[i])'
        eval(run_dotests)
        

