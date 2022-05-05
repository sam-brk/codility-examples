def solution(input):
    min = 1
    print(type(input))
    sortedInput = input.sort()
    for i in sortedInput:
        if i==min:
            min = min+1

    return min

