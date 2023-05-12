# teacher.py
#The enviornment should be in the folder where do_test.py is located.

# Under the environment
#Create a folder to store students answer and correct answers: 
#       same name as the function needs to be tested

#Under the folder we created before
#Create a file to store correct answer we created: 
#       teacher.py (can only use this name)

# In teacher.py:
#Teacher writes the function in teacher.py.
#Type annotation require on parameters
#Extra Tests section is optional
#Properties section is optional
#Rename Unit Tests to Extra Tests

def add2ints(a:int, b:int):
    """
    @Question statement
    
    Write a function that takes two ints as input and returns their sum.

    >>> add2ints(4, 7)
    11
    >>> add2ints(-1, 3)
    2
    >>> add2ints(0, -5)
    -5

    @Extra Tests 
    >>> add2ints(7, 8)
    15
    >>> add2ints(0, 0)
    0
    >>> add2ints(1, -1)
    0
    >>> add2ints(2, 2)
    4
    >>> add2ints(20, 14)
    34
    >>> add2ints(-26, 0)
    -26

    @Properties
    add2ints(a, b) == add2ints(b, a)
    add2ints(a, 0) == a
    add2ints(0, b) == b
    add2ints(a, -a) == 0
    Commutative
    """
    return a + b
