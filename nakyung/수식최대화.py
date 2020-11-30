def solution(expression):
    answer = 0
    list = []
    answer = eval(expression)
    str = ''
    for i in expression:
        if i != '*' and i != '+' and i != '-': 
            str += i
            list.append(str)
        else:
            str = ''
            list.append(i)
            
    print(list)
    operator = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('*', '-', '*'),
        ('-', '+', '*'),
        ('-', '*', '+')
    ]
    for i in operator:
        for j in list:
            if j == i[0]:
                #..?
    return answer
