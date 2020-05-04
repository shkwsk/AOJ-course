def main():
    n = int(input())
    rows = []
    for i in range(n):
        rows.append([int(x) for x in input().split()])
    for row in rows:
        u,k = row[0],row[1]
        ul = [0]*n
        for j in range(k):
            ul[row[j+2]-1] = 1
        print(' '.join([str(u) for u in ul]))

if __name__ == '__main__':
    main()
