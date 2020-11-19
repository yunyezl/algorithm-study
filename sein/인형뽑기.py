def solution(board, moves):
    
    answer = 0
    baguni = []

    for move in moves:
        for i in board:
            if i[move-1] != 0:
                baguni.append(i[move-1])
                i[move-1] = 0
                break

        if len(baguni) >= 2 and (baguni[-1] == baguni[-2]):
            del baguni[-2:]
            answer += 2
    
    return answer
