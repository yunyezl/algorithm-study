def solution(numbers, hand):
    answer = ''

    leftHand = '*'
    rightHand = '#'

    button = {0:(3, 1), 1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2),'*':(3, 0), '#':(3,2)}

    for n in numbers:
        if n in {1,4,7} :
            answer += 'L'
            leftHand = n
        elif n in {3,6,9} :
            answer += 'R'
            rightHand = n

        else:
            leftD = abs(button[n][0]-button[leftHand][0])+abs(button[n][1]-button[leftHand][1])
            rightD = abs(button[n][0]-button[rightHand][0])+abs(button[n][1]-button[rightHand][1])

            if leftD < rightD :
                answer += 'L'
                leftHand = n

            elif leftD > rightD :
                answer += 'R'
                rightHand = n

            else:
                answer += hand[0].upper()
                if hand == 'right' :
                    rightHand = n
                else: leftHand =n

    return answer
