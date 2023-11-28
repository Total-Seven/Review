function endZeros(a) {
    if (a == 0) return 1

    let res = 0
    while (!(a % 10)) {
        res++
        a = Math.floor(a / 10)
    }
    return res
}

console.log(endZeros(0))
console.log(endZeros(1))
console.log(endZeros(10))
console.log(endZeros(101))
console.log(endZeros(245))
console.log(endZeros(100100))