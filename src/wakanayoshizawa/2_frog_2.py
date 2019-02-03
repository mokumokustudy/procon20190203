N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * (N)

for i in range(1, N):
    if i > 1:
        _dp = []
        for j in range (1, K + 1):
            if N - i >= j:
                _dp.append(dp[i-j] + abs(h[i] - h[i-j]))
        dp[i] = min(_dp)
    elif i == 1:
        dp[i] = dp[i-1] + abs(h[i] - h[i-1])

print(dp[-1])