def remove_vowel(s):
    vowel="aeiouAEIOU"
    return ''.join([char for char in s if char not in vowel])
print(remove_vowel("hello world"))