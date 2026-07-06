def count_vowel(s):
    vowel='aeiouAEIOU'
    found=[char for char in s if vowel]
    print("vowels found",found)
    print(len(found))
