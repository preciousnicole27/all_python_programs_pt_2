# define the function that will convert the input into lower case
def lower_case_name():
# ask for user input 
# use while True loop
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        else:
            print("Please input a valid name:")
# turn input into lower case letters
    lower_case_name = full_name.lower()
# print full name in lower case
    print("Full name:", lower_case_name)
    
lower_case_name()