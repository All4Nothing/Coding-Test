while (l := input()) != '.':
        stack = []
        for s in l:
            match s:
                case '(':
                    stack.append(s)
                case ')':
                    try:
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            stack.append(s)
                    except:
                        stack.append(s)
                case '[':
                    stack.append(s)
                case']':
                    try:
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            stack.append(s)
                    except:
                        stack.append(s)
        print('no') if len(stack) else print('yes')