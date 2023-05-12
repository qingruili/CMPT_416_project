# combine_strings.py

def combine_strings(s:str, t:str, u:str):
    """
    @Question statement
     
    Write function that takes in three strings as input and returns them in a
    list with all letters converted to uppercase.

    >>> combine_strings('one', 'two', 'three')
    ['ONE', 'TWO', 'THREE']
    >>> combine_strings('alAA', 'aBa', 'cat')
    ['ALAA', 'ABA', 'CAT']
    >>> combine_strings('Apple', 'sa', 'uce!')
    ['APPLE', 'SA', 'UCE!']


    @Extra Tests
    >>> combine_strings('Gpe', '', '')
    ['GPE', '', '']
    >>> combine_strings('', '', '')
    ['', '', '']
    >>> combine_strings('a;Aple', 'baba', 'ckJJ')
    ['A;APLE', 'BABA', 'CKJJ']

    
    @Properties
    len(combine_strings(s, t, u)) == 3
    """
    return [s.upper(), t.upper(), u.upper()]
