def clean_text(text):
    """This misses upper-case letters.
    """
    cleaned_text = ''
    for char in text:
        if char in 'abcdefghijklmnopqrstuvwxyz': # oops, forgot to check upper-case
            cleaned_text += char # keep spaces and letters
        else:
            cleaned_text += ' '  # replace other characters with spaces
    return cleaned_text