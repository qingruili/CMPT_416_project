# combine_len.py

def combine_len(s:str, t:str, u:str):
    """
    @Question Statement
    
    Write a function that takes in three strings as input and returns a list of
    their lengths.

    >>> combine_len('one', 'two', 'three')
    [3, 3, 5]
    >>> combine_len('alAA', 'B', 'cat')
    [4, 1, 3]
    >>> combine_len('applesd', '', 'ct')
    [7, 0, 2]


    @Extra Tests
    >>> combine_len('Gpe', '', '')
    [3, 0, 0]
    >>> combine_len('', '', '')
    [0, 0, 0]
    >>> combine_len('a;Aple', 'baba', 'ckJJ')
    [6, 4, 4]


    @Properties
    len(combine_len(s, t, u)) == 3
    """
    return [len(s), len(t), len(u)]
