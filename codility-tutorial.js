function solution(A) {
    let min = 1
    const sortedInput = A.sort()
    sortedInput.forEach((i) => i===min && min++)
    return min
}
