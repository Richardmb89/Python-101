def unique_chars_in_string(input_string):
    for i in input_string:
        if input_string.count(i) > 1:
            return False

    return True

wordOne = "Python"
wordTwo = "Programming"

print("Tested Code:")
print("%d" %unique_chars_in_string(wordOne))
print("%d" %unique_chars_in_string(wordTwo))
