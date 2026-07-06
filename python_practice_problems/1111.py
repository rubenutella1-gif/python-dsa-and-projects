n = int(input())

mp = {}

for _ in range(n):
    sender, receiver, amount, time = input().split()
    amount = int(amount)
    time = int(time)

    # 🔥 Tuple key
    key = (sender, receiver, amount)

    if key in mp:
        for prev_time in mp[key]:
            if abs(time - prev_time) <= 60:
                print(sender, receiver, amount, time)
                break
        mp[key].append(time)
    else:
        mp[key] = [time]