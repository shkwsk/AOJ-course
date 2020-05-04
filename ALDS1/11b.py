def dfs(vum,v,d,f,t):
    # print('first')
    # print(vum,v,d,f,t)
    if f[v] >= 0:
        return d,f,t
    t += 1
    d[v] = t
    for u in vum[v]:
        # print(v, d[v], f[v], u, d[u], f[u])
        if d[u] >= 0:
            # print('skip', str(v), str(u))
            continue
        d,f,t = dfs(vum,u,d,f,t)
    t += 1
    f[v] = t
    # print(v, d[v], f[v])
    # print('last')
    # print(vum,v,d,f,t)
    return d,f,t

def main():
    n = int(input())
    rows = []
    for i in range(n):
        rows.append([int(x) for x in input().split()])

    vum = {}
    for v,row in enumerate(rows):
        u,k = row[0],row[1]
        ul = []
        if k > 0:
            for j in row[2:]:
                ul.append(j-1)
        vum.update({v:ul})

    # print(vum)
    d = [-1]*len(vum)
    f = [-1]*len(vum)
    t = 0
    for v in vum:
        d,f,t = dfs(vum,v,d,f,t)
    for i,(j,k) in enumerate(zip(d,f)):
        print(i+1,j,k)

if __name__ == '__main__':
    main()
