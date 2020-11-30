def solution(expression):
    answer = 0

    a = list(expression)
    a = list(set(a))
    a.sort()
    symbol = []
    allCalCase = [] # 연산자 우선순위를 저장하는 배열
    
    for i in a:
        if i in ['*', '-', '+']:
            symbol.append(i)
        else:
            break
    
    # 모든 경우의 수 만들기
    import copy
    if len(symbol) != 1:
        for j in symbol:
            temp = []
            temp.append(j)
            symbol2 = copy.deepcopy(symbol)
            symbol2.remove(j)
            for k in symbol2:
                temp.append(k)
            allCalCase.append(temp)
            temp2 = copy.deepcopy(temp)
            if len(symbol) > 2:
                temp2[len(symbol)-1], temp2[len(symbol)-2] = temp2[len(symbol)-2], temp2[len(symbol)-1]
            allCalCase.append(temp2)
    else:
        allCalCase = symbol
    print(allCalCase)

    allAnswer = [] # allCalCase에 있는 연산자 우선순위를 통해 연산한 결과를 저장
    s = ''
    exList = []
    for i in expression: # 수식을 배열로 나눔.
        if i not in ['*', '-', '+']:
            s += i
        else:
            exList.append(s)
            s = i
            exList.append(s)
            s = ''
    exList.append(s)

    for i in allCalCase:
        print("연산자 우선순위:", i)
        exList2 = copy.deepcopy(exList)
        for j in i:
            count = exList2.count(j)
            for k in range(count):
                index = exList2.index(j)
                if j == '+':
                    exList2[index] = int(exList2[index - 1]) + int(exList2[index + 1])
                    del exList2[index + 1]
                    del exList2[index - 1]
                elif j == '-':
                    exList2[index] = int(exList2[index - 1]) - int(exList2[index + 1])
                    del exList2[index + 1]
                    del exList2[index - 1]
                elif j == '*':
                    exList2[index] = int(exList2[index - 1]) * int(exList2[index + 1])
                    del exList2[index + 1]
                    del exList2[index - 1]
        exList2 = list(map(str, exList2))
        if len(exList2) > 1:
            if exList2[1] == '+':
                result = int(exList2[0]) + int(exList2[2])
            elif exList2[1] == '-':
                result = int(exList2[0]) - int(exList2[2])
            elif exList2[1] == '*':
                result = int(exList2[0]) * int(exList2[2])
        else:
            result = abs(int(exList2[0]))
        allAnswer.append(abs(result))
    return max(allAnswer)

