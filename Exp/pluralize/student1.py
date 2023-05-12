def pluralize(word):
    """Correct solution: should return the same results as the model solution.
    """
    if word == '': return 's'
    if word[-1] == 's': return word
    return word + 's'