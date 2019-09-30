#Algo 1.1: Traversing in Linear Array

#Step 01: Reading input
A = input("Enter elements of array, seperated by commas: ").split(",")
#Step 02: Setting initial values
R = 0 ; S = len(A); T = 1
#Step 03: Processing Array by Traversing
#(Suppose PROCESS == printing each element on screen)
for K in range(R, S, T):
    print(A[K])

#Alternate Method:

#Step 01: Reading input
A = input("Enter elements of array, seperated by commas: ").split(",")
#Step 02: Processing Array by Traversing
#(Suppose PROCESS == printing each element on screen)
for i in A:
    print(i)

