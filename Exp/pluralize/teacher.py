# pluralize.py

#
# Teacher writes this function.
#

def pluralize(s:str):
    """
    @Question statement
    
    Write a function that returns a copy of a copy of word with an 's' 
    added to the end. If word already ends in 's', return word unchanged.

    >>> pluralize('cat')
    'cats'
    >>> pluralize('dogs')
    'dogs'
    >>> pluralize('')
    's'
    
    @Properties 
    len(pluralize(s)) >= len(s)
    pluralize(s)[-1] == 's'
    """
    if s == '':
        return 's'
    elif s[-1] == 's':
        return s
    else:
        return s + 's'
