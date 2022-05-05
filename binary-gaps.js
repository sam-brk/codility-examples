function solution(N) {
    if(N<1){
        return 0
    }
    const binary = N.toString(2)
    const splitBinary = binary.split('')
    let binGap = 0
    const binGaps=[]

    for(let i=0;i<splitBinary.length;i++){
        if(splitBinary[i]==='1' && splitBinary[i+1] ==='0'){
            binGap++;
        }
        if(splitBinary[i]==='0' && splitBinary[i+1] ==='0'){
            binGap++;
        }
        if(splitBinary[i]==='0' && splitBinary[i+1] ==='1'){
            binGaps.push(binGap)
            binGap=0
        }
    }
    if(binGaps.length>0){
        return Math.max(...binGaps)
    } else {
        return 0
    }
}