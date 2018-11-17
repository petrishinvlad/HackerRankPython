def average(array):
    uniqueArray = set(array)
    return sum(uniqueArray)/len(uniqueArray)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
