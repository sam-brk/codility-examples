def binary_gaps(N):
    if N<1:
        return 0
    binary = format(N, 'b')
    binGaps = []
    binGap = 0
    for i in range(len(binary)-1):
        type(binary[i])
        if binary[i] == '1' and binary[i+1] == '0':
            binGap = binGap + 1
        if binary[i] == '0' and binary[i+1] == '0':
            binGap = binGap + 1
        if binary[i] == '0' and binary[i+1] == '1':
            type(binGap)
            binGaps.append(binGap)
            binGap = 0
    if len(binGaps) > 0:
        return max(binGaps)
    else:
        return 0
