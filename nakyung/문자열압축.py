#28번 테스트 케이스 안됨
def solution(s):
    split = []
    l = []
    n = 1
    for i in range(1, len(s)):
        if s[0:i] == s[i:i + i]:
            split.append(s[0:i])
    if len(split) > 0:
        for i in range(1, (len(s)//2)+1):
            s_demo = s
            arr = []
            for j in range((len(s)//i) if(len(s)%i)==0 else (len(s)//i)+1):
                if s[i*j:(i*j)+i]==s[(i*j)+i:(i*j)+2*i]:
                    n+=1
                else:
                    if n == 1:
                        arr.append(s[i*j:(i*j)+i])
                    else:
                        arr.append(str(n)+str(s[i*j:(i*j)+i]))
                        n = 1

            s_demo = ''.join(e for e in arr)
            l.append(len(s_demo))
            l.sort()
        return l[0]
    else:
        return len(s)
