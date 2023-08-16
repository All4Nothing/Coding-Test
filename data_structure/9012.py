for _ in range(int(input())):
    ps = input()
    while '()' in ps:
        ps.replace('()','')
    print('NO') if ps else print('YES')