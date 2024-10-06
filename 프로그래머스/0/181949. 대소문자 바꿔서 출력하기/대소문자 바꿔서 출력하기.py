str = input()
for i in str:
    if i.upper() == i:
        print(i.lower(), end = '')
    else:
        print(i.upper(), end = '')