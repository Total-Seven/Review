import re

value = "apple orange apple"

new_string = re.sub(
    r"(^|\s)\S", lambda match: match.group(0).upper(), value.lower())

print(new_string)
