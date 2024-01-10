from file2text.file2text import *

expected_word = 'Test WORD convert.'
actual_word = convert_word("tests/test.docx")

print(actual_word)
assert actual_word == expected_word, f"The actual output of 'convert_word' is {actual_word}"