def count_vowels(text):
    """Correct solution: should return the same results as the model solution.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count
