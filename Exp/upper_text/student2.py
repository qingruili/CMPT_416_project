def upper_text(text):
    """Error: e confused with 3
    """
    result = ''
    for c in text:
        if c in 'abcd3fghijklmnopqrstuvwxyz':  # e replace by 3
            result += chr(ord(c) - 32)
    return result
