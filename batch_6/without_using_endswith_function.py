# define the function
def check_suffix(text,suffix):
# use slicing
# use return function
    if len(suffix) > len(text):
        return False
    return text[-len(suffix):] == suffix
# ask for user for text and suffix input
text = input("Enter a text:")
suffix = input("Enter a suffix:")
# print the results
print(check_suffix(text,suffix))