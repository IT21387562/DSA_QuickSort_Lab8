A = []

for v in range(8):
    A.append(int(input("Enter Value : ")))
print(A)

def partition(A,p_low,r_high):
    x = A[r_high]
    i = (p_low -1)
    for j in range(p_low, r_high):
        if A[j] <= x:
           i=i+1
           A[i],A[j]=A[j],A[i]
    A[i+1],A[r_high]= A[r_high],A[i+1]
    return(i+1)

def quickSort(A,p_low,r_high):
    if p_low < r_low:
        q =  partition(A, p_low, r_high)
        quickSort(A,p_low,q-1)
        quickSort(A,q+1,r_high)

quickSort(A, 0 , len(A)-1)
print("Sorted")
for i in range(len(A)):
    print(A[i])
            
        
    
