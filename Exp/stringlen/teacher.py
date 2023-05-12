# stringlen.py

def stringlen(a:str, b:str, c:str):
    """
    @Question statement
    Write a function that takes in three strings as input and returns their total length.

    >>> stringlen('one', 'two', 'three')
    11
    >>> stringlen('al', 'aba', 'cat')
    8
    >>> stringlen('apples', 'baba', '?')
    11

    @Extra Tests
    >>> stringlen('ape', '', '')
    3
    >>> stringlen('', '', '')
    0
    >>> stringlen('aple', 'baba', 'ckjj')
    12

    @Properties
    stringlen(a, b, c) == stringlen(b, c, a)
    stringlen(a, a, a) == 3 * len(a)
    stringlen(a, b, c) >= 0
    """
    return len(a) + len(b) + len(c)