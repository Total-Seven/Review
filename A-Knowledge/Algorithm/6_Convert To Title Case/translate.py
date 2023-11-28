original_string = "abc123"
translation_table = str.maketrans("abc", "123")
new_string = original_string.translate(translation_table)
print(new_string)
