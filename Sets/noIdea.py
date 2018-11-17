if __name__=='__main__':
    n, m = input().split()
    happiness_array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(sum([(elem in A) - (elem in B) for elem in happiness_array]))
