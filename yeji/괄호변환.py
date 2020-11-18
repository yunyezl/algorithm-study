def isRightBracketString(u):
    left = 0
    right = 0
    for i in u: #u가 올바른 괄호 문자열인지 판단
        if left < right:
            return False # ) 의 개수가 더 많아지게 되면 올바르지 않은 문자열.
        if i == '(':
            left += 1
        else:
            right += 1
    else: #u가 올바른 문자열이라면(break가 한 번도 실행되지 않았다면) 
        return True

def divide(p):
    
    left = 0
    right = 0
    u = ''
    v = ''

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break

    return u, v


def solution(p):
    answer = ''

    if p == '':
        return ''

    u, v = divide(p)

    if isRightBracketString(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'

    u = u[1: -1]
    u = u.replace('(', '.')
    u = u.replace(')', '(')
    u = u.replace('.', ')')
    answer += u    

    return answer

    
