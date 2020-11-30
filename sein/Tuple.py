def solution(s):
    answer = []

    S = s[2:-2].split("},{")
    S.sort(key=lambda x: len(x))


    for t in S:
        l = list(map(int, t.split(',')))

        for add in l :
            if add not in answer :
                answer.append(add)

    print(answer)

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")