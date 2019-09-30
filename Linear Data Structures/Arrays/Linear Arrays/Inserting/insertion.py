#Algo 1.2: Insertion in Linear Array using Traversal of Indices

#Step 01: Reading input
#Suppose Upper Bound of the Array is 7
UB = 7
A = input("Enter the elements of the array, seperated by commas: ").split(",")
Value = input("Enter the value to be inserted: ")
K = int(input("Enter the position at which value is to be inserted: "))
#Step 02: Seperating Array into two parts
if len(A) < UB:
    unchange = A[:K]
    change = A[K:]
    A = unchange + [Value] + change
print(A)
    

#Alternate Method

#Step 01: Reading input
#Suppose Upper Bound of the Array is 7
UB = 7
A = input("Enter the elements of the array, seperated by commas: ").split(",")
Value = input("Enter the value to be inserted: ")
K = int(input("Enter the position at which value is to be inserted: "))
#Step 02: Inserting Element in Array
if len(A) < UB:
    A.insert(K, Value)
print(A)


    
