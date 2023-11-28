fn = password => {
    const cond0 = /password/i.test(password)
    const cond1 = password.length > 9
    const cond2 = password.length > 6
    const cond3 = /\d/.test(password)
    const cond4 = /\D/.test(password)

    console.log(cond0, cond1, cond2, cond3, cond4)

    if (cond0) return false
    else return cond1 || (cond2 && cond3 && cond4)
}

res = fn("PASSWORD12345")
console.log(res)