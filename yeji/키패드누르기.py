def solution(numbers, hand):
    answer = ''
    keypad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]

    leftP = (0, 3) # 첫 위치 *
    rightP = (2, 3) # 첫 위치 #

    for number in numbers:
        if number in keypad[0]: # 1, 4, 7
            leftP = (0, keypad[0].index(number))
            answer += 'L'
        elif number in keypad[2]: # 3, 6, 9
            rightP = (2, keypad[2].index(number))
            answer += 'R'
        else: # 가운데 있는 경우 거리 비교
            centerP = (1, keypad[1].index(number))
            leftDistance = abs(centerP[0]-leftP[0]) + abs(centerP[1]-leftP[1])
            rightDistance = abs(centerP[0]-rightP[0]) + abs(centerP[1]-rightP[1])
            if leftDistance < rightDistance:
                leftP = (1, keypad[1].index(number))
                answer += 'L'
            elif leftDistance > rightDistance:
                rightP = (1, keypad[1].index(number))
                answer += 'R'
            else:
                if hand == 'left':
                    leftP = (1, keypad[1].index(number))
                    answer += 'L'
                else:    
                    rightP = (1, keypad[1].index(number))
                    answer += 'R'

    return answer
