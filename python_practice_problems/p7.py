# input తీసుకోవడం
n = int(input("Enter n: "))      # positions
r = int(input("Enter r: "))      # values range
end = int(input("Enter end: "))  # last value

def count_arrangements(n, r, end):
    # DP table create
    dp = [[0]*(r+1) for _ in range(n+1)]

    # Step 1: first position must be 1
    dp[1][1] = 1

    # Step 2: fill remaining positions
    for i in range(2, n+1):
        total = sum(dp[i-1])   # previous row total

        for j in range(1, r+1):
            dp[i][j] = total - dp[i-1][j]

    # Step 3: return answer
    return dp[n][end]


# function call
result = count_arrangements(n, r, end)

# output print
print("Number of ways:", result)