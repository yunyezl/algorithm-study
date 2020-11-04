n = int(input())
store_list = input().split()
store_list = [int (i) for i in store_list]

m = int(input())
guest_list = input().split()
guest_list = [int (i) for i in guest_list]

for i in range(m):
    answer = []
    for j in range(n):
        if guest_list[i] == store_list[j]:
            answer.append(1)
            break
        else:
            answer.append(0)
    if 1 in answer:
        print("yes", end=" ")
    else:
        print("no", end=" ")
