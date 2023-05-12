# add_strings.py

def add_strings(s:str, t:str, u:str):
    """
    @Question statement
    
    Write a function that takes in three strings as input and returns them
    appended together as a single string with all letters are in uppercase.

    >>> add_strings('one', 'two', 'three')
    'ONETWOTHREE'
    >>> add_strings('apple', 'banaba', 'cat')
    'APPLEBANABACAT'
    >>> add_strings('alAA', 'aBa', 'cat')
    'ALAAABACAT'
    >>> add_strings('Apple', 'sa', 'uce!')
    'APPLESAUCE!'


    @Extra Tests 
    
    >>> add_strings('Gpe', '', '')
    'GPE'
    >>> add_strings('', '', '')
    ''
    >>> add_strings('a;Aple', 'baba', 'ckJJ')
    'A;APLEBABACKJJ'

    @Properties
    len(s) + len(t) + len(u) == len(add_strings(s, t, u))
    """
    return s.upper() + t.upper() + u.upper()