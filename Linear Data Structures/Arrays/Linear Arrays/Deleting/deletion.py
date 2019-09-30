#Algo 1.3: Deletion in Linear Array using Traversal of Indices

#Step 01: Reading input
#Suppose Lower Bound of the Array is 0
LB = 0
A = input("Enter the elements of the array, seperated by commas: ").split(",")
K = int(input("Enter the position at which value is to be deleted: "))
#Step 02: Seperating Array into two parts
if len(A) > LB:
    unchange = A[:K]
    change = A[(K+1):]
    A = unchange + change
print(A)


#Alternate Method

#Step 01: Reading input
#Suppose Lower Bound of the Array is 0
LB = 0
A = input("Enter the elements of the array, seperated by commas: ").split(",")
K = int(input("Enter the position at which value is to be deleted: "))
#Step 02: Seperating Array into two parts
if len(A) > LB:
    A.pop(K)

print(A)


