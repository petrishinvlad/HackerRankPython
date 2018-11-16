def count_substring(string, sub_string):
    substring_length = len(sub_string)
    return sum([1 for k in range(0, len(string) - substring_length + 1) if string[k:(k+substring_length)] == sub_string])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
