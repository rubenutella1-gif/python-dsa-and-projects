words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}

for word in words:
    key = "".join(sorted(word))

    if key not in anagrams:
        anagrams[key] = []

    anagrams[key].append(word)
a=list(anagrams.values())
for i in a:
    print(i,end=" ")