def clean_text(s:str):
    """
    @Question statement
    Write a function that replaces all non-alphabetic characters in text
    with spaces, keeping just letters and spaces.
    >>> clean_text('Hello, world!')
    'Hello  world '
    >>> clean_text('23 skidoo!')
    '   skidoo '
    >>> clean_text('a\\tb\\nc')
    'a b c'

    @Extra Tests
    >>> clean_text('Hello, world!') == 'Hello  world '
    True
    >>> clean_text('') == ''
    True

    @Properties
    len(s) == len(clean_text(s))
    Idempotent
    """
    cleaned_text = ''
    for char in s:
        if char.isalpha() or char == ' ':
            cleaned_text += char # keep spaces and letters
        else:
            cleaned_text += ' '  # replace other characters with spaces
    return cleaned_text
