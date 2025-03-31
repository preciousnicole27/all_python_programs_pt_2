# define the function that will convert the input into lower case
def lower_case():
# ask for user input 
# use while True loop
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
# turn input into lower case letters
# print full name in lower case