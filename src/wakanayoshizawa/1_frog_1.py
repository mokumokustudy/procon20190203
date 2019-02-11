N = int(input())
h = list(map(int, input().split()))

dp = [0] * (N)

for i in range(1, N):
    if i > 1:
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))
    elif i == 1:
        dp[i] = dp[i-1] + abs(h[i] - h[i-1])

print(dp[-1])