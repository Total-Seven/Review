import re


def toTitleCase_1(value):
    return re.sub(
        r"(^|\s)\S", lambda match: match.group(0).upper(), value.lower())


print(toTitleCase_1("typescript is great") == "Typescript Is Great")
print(toTitleCase_1("the answer is 42") == "The Answer Is 42")
print(toTitleCase_1("to be or not to be") == "To Be Or Not To Be")
print(toTitleCase_1("that is the question") == "That Is The Question")
print(toTitleCase_1("") == "")
