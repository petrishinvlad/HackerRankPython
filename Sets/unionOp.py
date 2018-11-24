if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    res = len(A.union(B))
    print(res)
