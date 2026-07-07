def reversed_sentence(sentence):
    s=sentence.split()
    s1=s[::-1]
    return ' '.join(s1)
print(reversed_sentence("Helllo This Is Python World"))