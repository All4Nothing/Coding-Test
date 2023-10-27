def BNP(seed, price):
    m = seed
    c = 0
    for p in price:
        temp = m//p
        m -= temp*p
        c += temp
    return c, m

def TIMING(seed, price):
    m = seed
    up = 0
    down = 0
    c = 0
    for i in range(1, len(price)):
        if price[i] > price[i-1]:
            up += 1
            down = 0
        elif price[i] < price[i-1]:
            down += 1
            up = 0
        if up > 2:
            m += c * price[i]
            c = 0
        elif down > 2:
            temp = m//price[i]
            m -= temp*price[i]
            c += temp
    return c, m

seed = int(input())
price = list(map(int, input().split()))
j_c, j_m = BNP(seed, price)
j = j_c*price[-1] + j_m
s_c, s_m = TIMING(seed, price)
s = s_c*price[-1] + s_m

if j > s:
    print('BNP')
elif j < s:
    print('TIMING')
else:
    print('SAMESAME')