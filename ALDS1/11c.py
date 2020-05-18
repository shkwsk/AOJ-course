import queue

def main():
    n = int(input())
    rows = []
    for i in range(n):
        rows.append([int(x) for x in input().split()])

    vum = {}
    for row in rows:
        u,k = row[0],row[1]
        ul = []
        if k > 0:
            for j in row[2:]:
                ul.append(j)
        vum.update({u:ul})
    # print(vum)

    ### bfs ###
    q = queue.Queue()
    D = [-1]*n # 最短距離
    s = 1 # 始点
    step = 0
    D[s-1] = step
    while True:
        # print('s',str(s))
        step = D[s-1] + 1
        for v in vum[s]:
            # print('v',str(v))
            if D[v-1] < 0:
                # print('append v',str(v),str(step))
                q.put(v)
                D[v-1] = step
        if q.empty():
            break
        # print(list(q.queue),V)
        s = q.get()

    for i,d in enumerate(D):
        print(str(i+1),d)

if __name__ == '__main__':
    main()
