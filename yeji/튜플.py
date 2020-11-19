def solution(s):
    answer = []
    tupleDic = {} # 각 숫자마다의 개수를 저장하는 딕셔너리
    
    s = s[2:-2].replace('}','').replace('{','').split(',')
    uniqueS = set(s)

    for i in uniqueS:
        tupleDic[i] = s.count(i)

    s = sorted(tupleDic.items(), key=lambda x: x[1], reverse=True)

    for j in s:
        answer.append(int(j[0]))
        
    return answer
