def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move = move - 1 #인덱스 
        for i in range(len(board)):
            if board[i][move] != 0:
                basket.append(board[i][move])
                board[i][move] = 0
                break
        last = len(basket) - 1
        if len(basket) >= 2 and (basket[last] == basket[last - 1]):
            basket.pop(last)
            basket.pop(last - 1)
            answer += 2
    
    return answer
