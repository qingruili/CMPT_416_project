def clean_text(text):
    """This returns the wrong string.
    """
    cleaned_text = ''
    for char in text:
        if char.isalpha():
            cleaned_text += char # keep spaces and letters
        else:
            cleaned_text += ' '  # replace other characters with spaces
    return text  # oops, should return cleaned_text