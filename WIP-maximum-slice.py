def solution(A):
    max_value = -2147483648
    for p in range(len(A)):
        for q in range(p, len(A)):
            slc = A[p:q]
            max_value = max(max_value, sum(slc))
    return max_value