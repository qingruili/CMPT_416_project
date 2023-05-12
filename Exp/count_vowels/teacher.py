def count_vowels(s:str):
    """
    Write a function that returns the number of vowels (a, e, i, o, u) in the input text.
    Count both uppercase and lowercase vowels.

    >>> count_vowels('seesaw')
    3
    >>> count_vowels('ABCDe')
    2
    >>> count_vowels('Python is awesome!')
    6
    
    @Extra Tests 
    >>> count_vowels('')
    0
    >>> count_vowels('why')
    0
    >>> count_vowels('aeiou')
    5
    >>> count_vowels('AEIOU')
    5
    
    @Properties
    0 <= count_vowels(s) <= len(s)
    """
    vowels = 'aeiou'
    count = 0
    for c in s.lower():
        if c in vowels:
            count += 1
    return count