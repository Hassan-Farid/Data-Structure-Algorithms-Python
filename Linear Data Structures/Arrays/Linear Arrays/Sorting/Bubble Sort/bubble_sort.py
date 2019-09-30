#Algo 1.4.1: Sorting Linear Array by Bubble Sort (Ascending Order)

#Step 01: Reading input
A = input("Enter the elements of an unsorted array, seperated by commas: ").split(",")
#Step 02: Performing Bubble Sort
for i in range(0, len(A)-1, 1):
    #[a. Comparing each element, decrementing total elements each time by 1]
    for j in range(0, len(A)-i-1,1):
        #[b. Comparing if greater, than swap]
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print(A)

