def solution(A):
    type(A)
    # Handle empty list
    if len(A)<1:
        return 0

    # Handle non lists, maybe redundant here...
    if type(A) is not list:
        print('not a list')
        return 0

    # Handle lists with only one value
    if max(A)==0 or min(A)==1:
        return 0
    
    if(max(A)>1 or min(A)<0):
        raise Exception("Invalid input, input should consist of only 0,1!")


    elements = {}

    for item in A:
        if item in elements: 
            elements[item] = elements[item]+1
        else:
            elements[item] = 1
    if(elements[0]>elements[1]):
        return elements[1]
    else:
        return elements[0]    
    raise Exception("This code should not be reachable!")