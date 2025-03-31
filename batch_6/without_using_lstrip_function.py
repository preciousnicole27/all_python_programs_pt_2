# process and define the input to remove leading spaces
def remove_leading_spaces(text):
# use loop
    index = 0
# init index
    while index < len(text) and text [index] == " ":
        index += 1
# use slicing
    return text[index:]
# get user input 
# print results