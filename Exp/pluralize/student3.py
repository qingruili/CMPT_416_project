def pluralize(word):
    """Error: doesn't check for empty word
    """
    if word[-1] == 's': return word
    return word + 's'