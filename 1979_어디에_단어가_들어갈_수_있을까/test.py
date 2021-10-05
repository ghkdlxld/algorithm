def counting_sort(A, B, k):
    A = range(1, k+1)
    B = []*len(A)
    C = [0]*k

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]