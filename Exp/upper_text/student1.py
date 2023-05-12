def upper_text(text):
    """Should return the same results as the model solution.
    """
    result = ''
    for c in text:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result
