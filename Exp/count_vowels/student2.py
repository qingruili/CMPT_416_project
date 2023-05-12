def count_vowels(text):
    """Error: only counts lowercase vowels
    """
    vowels = 'aeiou'
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count
