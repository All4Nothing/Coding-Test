def solution(edges):
    ans = [0, 0, 0, 0]
    dic = {}
    r_dic = {}
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
            
        if b in r_dic:
            r_dic[b].append(a)
        else:
            r_dic[b] = [a]
    
    # find created node
    ## created node : 나가는 선만 있고, 들어오는 선은 없음
    for key in dic:
        if (len(dic[key]) > 1) and (key not in r_dic):
            ans[0] = key
            break  
    
    # find stick
    ## stick : 들어오는 선은 하나 있는데, 나가는 선은 없는 노드가 존재함
    for node in r_dic:
        if node not in dic:
            ans[2] += 1
            
    # find 8
    ## 8 : 나가는 선이 2개, 들어오는 선이 2개인 노드가 존재함
    for node in dic:
        if node != key:
            if len(dic[node]) > 1 and len(r_dic[node]) > 1:
                ans[3] += 1
    
    # count donut
    ## donut : 그래프는 정점의 나가는 선 수 만큼 존재함
    ans[1] += len(dic[key]) - ans[2] - ans[3]
    
    return ans