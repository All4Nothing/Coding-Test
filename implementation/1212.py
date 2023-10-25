def octal_to_binary(n):
    num = n
    arr = []
    for _ in range(3):
        arr.append(str(num%2))
        num = num // 2
    b = ''.join(arr[::-1])
    return b

n = input()
l = []
for i in n:
    l.append(octal_to_binary(int(i)))
print(int(''.join(l))) 