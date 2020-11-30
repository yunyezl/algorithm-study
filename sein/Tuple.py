def solution(s):
    answer = []

    split_s = s[2:-2].split("},{")
    split_s.sort(key=lambda x: len(x))

    for t in split_s:
        l = list(map(int, t.split(',')))
        for add in l :
            if add not in answer :
                answer.append(add)

    return answer
