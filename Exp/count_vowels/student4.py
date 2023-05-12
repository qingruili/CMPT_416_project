def count_vowels(text):
    """Error: returns at end of for-loop
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for c in text:
        if c in vowels:
            count += 1
        return count
