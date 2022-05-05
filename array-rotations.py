def solution(input, numOfRotations):
    if len(input) == 0:
        return input
    for i in range(numOfRotations):
        indexOfLastElement = len(input)-1
        rotatedElement = input[indexOfLastElement]
        input.pop(len(input)-1)
        input.insert(0,rotatedElement)
    return input