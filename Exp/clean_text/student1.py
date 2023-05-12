def clean_text(text):
    """This is misses checking for a space in the if-statement.
    Should return the same results as the model solution.
    """
    cleaned_text = ''
    for char in text:
        if char.isalpha(): # oops, forgot to check for space
            cleaned_text += char # keep spaces and letters
        else:
            cleaned_text += ' '  # replace other characters with spaces
    return cleaned_text