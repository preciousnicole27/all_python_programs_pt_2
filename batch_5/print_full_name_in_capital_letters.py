# define the function that will convert input into capital letters
def capital_letters():
# ask for user input
# use while true loop 
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print("Please input a valid name:")
# turn input into capital letters
# print full name in capital letters