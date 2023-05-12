# upper_text.py

#
# Teacher writes this function.
#

def upper_text(s:str):
    """
    @Question statement
    
    Write a function that returns a copy of text with all lowercase characters
    a-z replaced by their uppercase versions A-Z. Leave all other characters
    unchanged.

    Calling upper_text(text) should always return the same thing as
    text.upper(). Do NOT use the upper() method anywhere in your solution.

    >>> upper_text('cat')
    'CAT'
    >>> upper_text('Sam!')
    'SAM!'
    >>> upper_text('1 TWO 3 four')
    '1 TWO 3 FOUR'
    
    @Extra Tests

    >>> upper_text('Hello, world!')
    'HELLO, WORLD!'

    >>> upper_text('')
    ''

    
    @Properties
    len(s) == len(upper_text(s))
    Idempotent
    """
    return s.upper()