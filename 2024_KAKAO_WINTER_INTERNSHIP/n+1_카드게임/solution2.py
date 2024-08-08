rounds = []
import copy

def dfs(n, coin, my_cards, left_cards, r, check_double, flag):
    global rounds
    f = flag[:]# copy.deepcopy(flag)

    if check_double:
        is_break = 0
        for i in range(len(my_cards)):
            remove_i = my_cards[i]
            if not f[remove_i]:
                continue
            for j in range(i+1, len(my_cards)):
                remove_j = my_cards[j]
                if not f[remove_j]:
                    continue
                if my_cards[i] + my_cards[j] == n+1:
                    f[remove_i] = 0
                    f[remove_j] = 0
                    is_break = 1
                    break
            if is_break:
                break
        if not is_break:
            rounds.append(r)
            return True

        if len(left_cards) == 0:
            rounds.append(r+1)
            return True
        else:
            if coin:
                dfs(n, coin-1, my_cards+[left_cards[0]], left_cards[1:], r+1, 0, f)
            dfs(n, coin, my_cards, left_cards[1:], r+1, 0, f)
    else:
        if coin:
            dfs(n, coin-1, my_cards+[left_cards[0]], left_cards[1:], r, 1, f)
        dfs(n, coin, my_cards, left_cards[1:], r, 1, f)

    

def solution(coin, cards):
    n = len(cards)
    my_cards = cards[:n//3]
    left_cards = cards[n//3:]
    flag = [1 for _ in range(len(cards)+1)]

    if coin:
        dfs(n, coin-1, my_cards+[left_cards[0]], left_cards[1:], 1, 0, flag)
    dfs(n, coin, my_cards, left_cards[1:], 1, 0, flag)
    return max(rounds)