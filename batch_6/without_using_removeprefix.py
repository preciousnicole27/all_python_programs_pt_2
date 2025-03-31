# process the function to remove prefix
def remove_prefix(text, prefix):
# init index
    index = 0
# check if input starts with a prefix
    while index < len(prefix) and index < len(text) and text [index]:
        index += 1
# use slicing 
    return text[index:]
# ask for user input
text = input("Enter a text:")
prefix = input("Enter the prefix:")
# print input with the removed prefix
print(remove_prefix(text, prefix))