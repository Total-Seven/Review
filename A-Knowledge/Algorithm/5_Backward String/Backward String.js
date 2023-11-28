function backwardString(value) {
    let newStr = ""
    for (let char of value) {
        newStr = char + newStr
    }
    return newStr
}

console.log(backwardString("val"))
console.log(backwardString(""))
console.log(backwardString("ohho"))
console.log(backwardString("123456789"))