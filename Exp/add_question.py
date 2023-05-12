import sys
import os
from extract_path import *

def create_question_folder(name):

    question_folder_path = __file__

    last_position = extract_path(question_folder_path)


    question_folder_path = question_folder_path[:last_position+1]+name

    
    f_path = os.path.join(os.path.dirname(question_folder_path), name)


    if not os.path.exists(f_path):
        os.makedirs(f_path)
    
    file_path = os.path.join(f_path, "teacher.py")
    
    inner_function_str = f'''
# teacher.py

# put parameters in the function definition; use type annotations, e.g.
# def {name}(a:int, b:int):

def {name}(x):
    """
    @Question statement
    (describe question here; include some doctests)

    @Extra Tests
    (optional doctests, not seen by student until they get marking back)

    @Properties
    (optional)
    """
    # put correct solution code here
    pass
    '''

    with open(file_path, "w") as f:
        f.write(inner_function_str)
    



create_question_folder(sys.argv[1])