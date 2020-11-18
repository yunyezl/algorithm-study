def solution(s):
    answer = 0
    allCompressionList = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)):
        spiltList = [s[j:j+i] for j in range(0, len(s), i)]
        count = 0
        for k in range(len(spiltList)):
            if k+1 != len(spiltList):
                if (spiltList[k] == spiltList[k+1]):
                    spiltList[k] = ''
                    count += 1
                else:
                    count += 1
                    if count > 1:
                        spiltList[k] = str(count) + spiltList[k]
                    count = 0
            else:
                if count > 0:
                    count += 1
                    if count != 1:
                        spiltList[k] = str(count) + spiltList[k]
        allCompressionList.append(''.join(spiltList))

    return min(len(i) for i in allCompressionList)
