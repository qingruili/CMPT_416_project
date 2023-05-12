# lower_text.py

#
# Teacher writes this function.
#

def lower_text(s:str):
    """
    @Question statement
    
    Write a function that returns a copy of text with all uppercase characters
    A-Z replaced by their lowercase versions a-z. Leave all other characters
    unchanged.

    Calling lower_text(text) should always return the same thing as
    text.lower(). Do NOT use lower() anywhere in your solution.

    >>> lower_text('CAT')
    'cat'
    >>> lower_text('Sam!')
    'sam!'
    >>> lower_text('1 two 3 FOUR')
    '1 two 3 four'
    
    @Extra Tests 
    >>> lower_text('Hello, world!')
    'hello, world!'
    
    >>> lower_text('')
    ''
     
    
    @Properties 
    len(s) == len(lower_text(s))
    Idempotent
    """
    return s.lower()