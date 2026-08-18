while True:
    name1 = input("Enter your first name: ").lower().replace(" ", "")
    name2 = input("Enter your second name: ").lower().replace(" ", "")

    list1 = list(name1)
    list2 = list(name2)

    for char in name1:
        if char in list2:
            list1.remove(char)
            list2.remove(char)

    count = len(list1) + len(list2)

    print("Remaining characters:", list1 + list2)
    print("Count:", count)

    flames = ["F", "L", "A", "M", "E", "S"]

    index = 0

    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    print("FLAMES result:", flames[0])

    result = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    print("Relationship:", result[flames[0]])