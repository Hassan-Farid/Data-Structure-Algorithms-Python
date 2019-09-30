#Algo 1.4.2: Sorting Linear Array using Selection Sort (Ascending Order)

#Step 01: Reading input
A = input("Enter elements of unsorted array, seperated by commas: ").split(",")
#Step 02: Performing Selection Sort Procedure
for i in range(0, len(A), 1):
    #[a. Setting pointer for item to be compared]
    k = i
    #[b. Comparing item with every other element of the array]
    for j in range(k+1, len(A), 1):
        #[c. If some other element greater than item, than update pointer value]
        if A[k] > A[j]:
            k = j
    if k != i:
        #[d. If pointer value not as same as before, swap elements]
        A[k], A[i] = A[i], A[k]

print(A)
