def solution(A):
    if len(A)<1:
        return 0
    sizeOfArray = len(A)
    elements = {}
    for i in range(sizeOfArray):
        element = str(A[i])
        if element in elements:
            elements[element] = elements[element]+1
        else:
            elements[element] = 1
    returnedElement = 0
    for element in elements:
        if(elements[element] %2 == 1):
            returnedElement = int(element)
    return returnedElement