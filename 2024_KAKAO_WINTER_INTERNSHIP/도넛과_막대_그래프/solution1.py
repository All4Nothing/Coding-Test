typ = None

def patrol(dic, flag, key):
    global typ
    if key in dic:
        for k in dic[key]: # [5, 8]
            # print("key: ",key)
            # print("k: ", k)
            # print("flag: ", flag)
            if flag[k]:
                if len(dic[k]) > 1 or len(dic[key]) > 1:
                    # print("8 key: ",key, "k: ", k)
                    typ = 3 # 8
                    return True
                else:
                    # print("D key, k", key, k)
                    typ = 1 # Donut
                    return True
            else:
                flag[k] = 1
                if k in dic:
                    patrol(dic, flag, k)
                else:
                    # print("S key, k", key, k)
                    typ = 2 # stick
                    return True
    else:
        typ = 2 # stick
        return True
                    
    return True

def solution(edges):
    ans = [0, 0, 0, 0]
    dic = {}
    r_dic = {}
    flag = {}
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
            flag[a] = 0
            
        if b in r_dic:
            r_dic[b].append(a)
        else:
            r_dic[b] = [a]
            flag[b] = 0
    
    # find created node
    for key in dic:
        if (len(dic[key]) > 1) and (key not in r_dic):
            ans[0] = key
            flag[key] = 1
            break  
    
    #print("dictionary: ", dic)
    #print("r_dictionary: ", r_dic)
    #print("flag: ", flag)
    #print("="*10)

    for k in dic[key]:
        patrol(dic, flag, k)
        ans[typ] += 1
        # print("ans: ", ans)
        #print("k & patrol typ: ", k ,typ)
    #print("answer :", ans)
    return ans