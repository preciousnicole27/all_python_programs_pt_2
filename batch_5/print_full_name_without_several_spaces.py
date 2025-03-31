# ask for user input 
# define the function that remove the leading spaces
def remove_leading_spaces():
# use while loop to ask for input
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print("Please input a valid full name:")
# print if the input is invalid
# display the full name without the leading spaces

remove_leading_spaces()