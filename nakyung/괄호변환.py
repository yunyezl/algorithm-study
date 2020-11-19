#미완성
def solution(p):
    result = [0]*1000
    u = []
    list_p = []
    num = []
    if p == '':
        return ''
    else:
        for i in range(len(p)):
            list_p.append(p[i])
        for i in range(len(list_p)-1):
            if list_p[i] == '(' and list_p[i+1] == ')':
                num.append(i)
                result[i] = list_p[i] + list_p[i+1]
                return result
                # if num[0] == 0:
                #     u = list_p[i] + list_p[i+1]
                #     result.append(u)
                #     v = list_p[i+2:]
                #     del num[0]
                #     solution(v)
                #     break
