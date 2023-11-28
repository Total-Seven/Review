function toTitleCase_1(value) {
    return value.toLowerCase().replace(/(^|\s)\S/g, match => match.toUpperCase())
}

function toTitleCase_2(value) {
    return value
        .split(" ")
        .map(word => word = word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(" ")
}

console.log(toTitleCase_1("typescript is great") == "Typescript Is Great");
console.log(toTitleCase_1("the answer is 42") == "The Answer Is 42");
console.log(toTitleCase_1("to be or not to be") == "To Be Or Not To Be");
console.log(toTitleCase_1("that is the question") == "That Is The Question");
console.log(toTitleCase_1("") == "");

console.log(toTitleCase_2("typescript is great") == "Typescript Is Great");
console.log(toTitleCase_2("the answer is 42") == "The Answer Is 42");
console.log(toTitleCase_2("to be or not to be") == "To Be Or Not To Be");
console.log(toTitleCase_2("that is the question") == "That Is The Question");
console.log(toTitleCase_2("") == "");