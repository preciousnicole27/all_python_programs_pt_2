# define a function
def justified_text(text,width):
# check text length
# return text
    if len(text) >= width:
        return text
# add spaces
    return text + " " * (width - len(text))
# ask for user input
text = input("Enter a text:")
width = int(input("Enter a width:"))
# print justified text