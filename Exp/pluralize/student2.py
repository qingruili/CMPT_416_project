def pluralize(word):
    """Error: does not add 's' to the end.
    """
    if word == '': return ''
    if word[-1] == 's': return word
    return word