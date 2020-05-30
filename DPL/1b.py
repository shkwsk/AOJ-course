def main():
    N,W = [int(x) for x in input().split()]
    vl,wl = [],[]
    for _ in range(N):
        v,w = [int(x) for x in input().split()]
        vl.append(v)
        wl.append(w)

    dp = []
    for i in range(N+1):
        dp.append([0]*(W+1))

    for i in range(N):
        for j in range(W+1):
            # print(i,j)
            if j < wl[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i][j-wl[i]]+vl[i])
            # print(dp)
    print(int(dp[N][W]))


if __name__ == '__main__':
    main()
