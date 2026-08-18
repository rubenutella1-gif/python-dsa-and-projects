def count_vowel(s):
    vowel = "aeiouAEIOU"
    found = [char for char in s if char in vowel]

    print("Vowels found:", found)
    print("Count:", len(found))
s=input()
count_vowel(s)