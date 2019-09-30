#Algo 1.4.3: Sorting a Linear Array using Insertion Sort (Ascending Order)

#Step 01: [Reading input]
A = input("Enter elements of unsorted array, sepearted by commas: ").split(",")
#Step 02: [Applying Insertion Sort Procedure]
for i in range(1, len(A), 1):
    #[a. Initializing element being compared to]
    x = A[i]
    #[b. Initializing position of item to be compared]
    j = i-1
    #[c. If item greater than other element, swap positions until sorted]
    while A[j] > x and j >= 0:
        A[j+1] = A[j]
        j = j-1
    #[d. Assigning the next item to the initial element of comparision]
    A[j+1] = x
    
print(A)

