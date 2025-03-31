# define the function
def convert_to_lowercase_letters(text):
# convert the input into lowercase letters
    return text.casefold()
# ask for user input
text = input("Enter an input:")
# print the result
print(convert_to_lowercase_letters(text))