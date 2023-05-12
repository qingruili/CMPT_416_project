def lower_text(text):
    """Error: O confused with 0
    """
    result = ''
    for c in text:
        if c in 'ABCDEFGHIJKLMN0PQRSTUVWXYZ': # O replace by 0
            result += chr(ord(c) + 32)
    return result
