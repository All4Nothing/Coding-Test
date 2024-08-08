rounds = []

def dfs(n, coin, my_cards, left_cards, r, check_double):
    global rounds
    
    if check_double:
        is_break = 0
        for i in range(len(my_cards)): # [0, 1, 2]
            for j in range(i, len(my_cards)): # [1, 2]
                if my_cards[i] + my_cards[j] == n+1:
                    remove_i = my_cards[i]
                    remove_j = my_cards[j]
                    my_cards.remove(remove_i)
                    my_cards.remove(remove_j)
                    is_break = 1
                    break
            if is_break:
                break
        if not is_break:
            rounds.append(r)
            return True

        if len(left_cards) == 0:
            print("r: ", r)
            print("coin: ", coin)
            print("my_cards: ", my_cards)
            print("left_cards: ", left_cards)
            rounds.append(r+1)
            return True
        else:
            if coin:
                dfs(n, coin-1, my_cards+[left_cards[0]], left_cards[1:], r+1, 0)
            dfs(n, coin, my_cards, left_cards[1:], r+1, 0)
    else:
        if coin:
            dfs(n, coin-1, my_cards+[left_cards[0]], left_cards[1:], r, 1)
        dfs(n, coin, my_cards, left_cards[1:], r, 1)

    

def solution(coin, cards):
    n = len(cards)
    my_cards = cards[:n//3]
    left_cards = cards[n//3:]
    if coin:
        dfs(n, coin-1, my_cards+[left_cards[0]], left_cards[1:], 1, 0)
    dfs(n, coin, my_cards, left_cards[1:], 1, 0)
    print("rounds: ", rounds)
    return max(rounds)