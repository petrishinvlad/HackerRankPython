if __name__=='__main__':
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    print ("\n".join(map(str ,sorted(B.difference(A).union(A.difference(B))))))
