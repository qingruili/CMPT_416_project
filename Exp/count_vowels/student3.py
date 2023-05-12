def count_vowels(text):
    """Error: vowels and text swapped.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for c in vowels:
        if c in text:
            count += 1
    return count