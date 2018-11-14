if __name__ == '__main__':
    data = [[input(), float(input())] for _ in range(int(input()))]
    score = sorted({s[1] for s in data})[1]
    result = sorted(s[0] for s in data if s[1] == score)
    print('\n'.join(result))