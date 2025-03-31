# define the function that will convert input into snake case
def snake_case():
# ask user for input
# use loop
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
    else:
        print("Enter a valid name:")
# convert input using snake casing
    snake_cased_name = full_name.lower().replace(" ", "_")
# print full name in snake case