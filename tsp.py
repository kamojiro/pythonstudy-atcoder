def tsp(K, G, INF=10**10):
    # K: vertex
    # G[i][j]: the distance from i to j
    # 任意の位置からスタートして全部回りきるまでの距離
    # 元の位置には戻ってこない
    dp = [[INF]*(1 << K) for _ in range(K)]
    for i in range(K):
        dp[i][1 << i] = 0

    for s in range(1 << K):
        for frm in range(K):
            if not s & 1 << frm: # 0 = False
                continue
            if dp[frm][s] == INF:
                continue
            for to in range(K):
                t = s | 1 << to
                if s == t:
                    continue
                dp[to][t] = min(dp[to][t], dp[frm][s] + G[frm][to])
    return min([dp[i][(1 << K) -1] for i in range(K)])
