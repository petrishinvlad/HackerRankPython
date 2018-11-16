if __name__ == '__main__':
    s = input()
    for func in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any([eval("character." + func + "()") for character in s]))
