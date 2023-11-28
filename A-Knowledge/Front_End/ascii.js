// const char = 'A';
// console.log(`小写字符与大写字符的ASCII码相差: ${"a".charCodeAt() - "A".charCodeAt()}`);
// console.log(`小写字符与大写字符的ASCII码相差: ${"z".charCodeAt() - "Z".charCodeAt()}`);

// console.log(/[a-z]/.test("hello"))

function toTitleCase(sentence) {
    let words = sentence.split(" ")
    for (let index in words) {
        let word = words[index]
        let new_word = ""
        for (let indey in words[index]) {
            let c = word[indey]
            if (indey == 0) {
                if (/[a-z]/.test(c)) new_word += String.fromCharCode(c.charCodeAt() - 32)
                else new_word += c
            }
            else if (/[A-Z]/.test(c)) {
                new_word += String.fromCharCode(c.charCodeAt() + 32)
            }
            else if (indey != 0) {
                new_word += c
            }
        }
        words[index] = new_word
    }
    return words.join(" ");
}
// console.log(toTitleCase("hello world"))
// console.log(toTitleCase("THE QUICK BROWN FOX"))
// console.log(toTitleCase("The Answer Is 42"))

/**
 * return sentence
 *      .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(' ');
 */

console.log("".charAt(0))
console.log(""[0])