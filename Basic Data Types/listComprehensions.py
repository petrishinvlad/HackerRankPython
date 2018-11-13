if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = []
    #solution 1
    for i1 in range(x + 1):
        for i2 in range(y + 1):
            for i3 in range(z + 1):
                if (i1+i2+i3 != n):
                    coordinate = [i1, i2, i3]
                    result.append(coordinate)
    print(result)
    #solution 2
    print ([[i1, i2, i3] for i1 in range(x+1) for i2 in range(y+1) for i3 in range(z+1) if (i1 + i2 + i3 != n)])
