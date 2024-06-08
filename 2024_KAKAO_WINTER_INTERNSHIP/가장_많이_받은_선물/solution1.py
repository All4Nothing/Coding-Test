# 2024 KAKAO WINTER INTERNSHIP
## 가장 많이 받은 선물

def solution(friends, gifts):
    n = len(friends)
    table = [[0 for _ in range(n)] for _ in range(n)]
    r_table = [[0 for _ in range(n)] for _ in range(n)]
    answer = [0 for _ in range(n)]

    # create table
    for relation in gifts:
        giver, reciver = relation.split()
        giver_idx = friends.index(giver) # friends.find(giver)
        reciver_idx = friends.index(reciver)
        
        table[giver_idx][reciver_idx] += 1
        r_table[reciver_idx][giver_idx] += 1
        
    # compute
    for g_idx in range(n):
        for r_idx in range(g_idx+1, n):
            if table[g_idx][r_idx] > table[r_idx][g_idx]:
                answer[g_idx] += 1
            elif table[g_idx][r_idx] < table[r_idx][g_idx]:
                answer[r_idx] += 1
            else:
                n1 = sum(table[g_idx]) - sum(r_table[g_idx])
                n2 = sum(table[r_idx]) - sum(r_table[r_idx])
                if n1 > n2:
                    answer[g_idx] += 1
                elif n1 < n2:
                    answer[r_idx] += 1
    return max(answer)