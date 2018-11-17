def average(array):
    unique_array = set(array)
    return sum(unique_array)/len(unique_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
