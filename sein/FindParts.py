import sys

input_N = input()
input_N_list = sys.stdin.readline().rstrip()

input_M = input()
input_M_list = sys.stdin.readline().rstrip().split(" ")

for x in input_M_list :
    if x in input_N_list :
        print("yes", end=" ")
    else:
        print("no", end=" ")
