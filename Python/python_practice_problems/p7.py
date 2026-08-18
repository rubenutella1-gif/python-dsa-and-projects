n = int(input("Enter n: "))      # positions
r = int(input("Enter r: "))      # values range
end = int(input("Enter end: "))  # last value

def count_arrangements(n, r, end):
    dp = [[0]*(r+1) for _ in range(n+1)]

    dp[1][1] = 1

    for i in range(2, n+1):
        total = sum(dp[i-1])   

        for j in range(1, r+1):
            dp[i][j] = total - dp[i-1][j]

    return dp[n][end]

result = count_arrangements(n, r, end)

print("Number of ways:", result)