# define the function that will fixed the improper casing to proper casing
def proper_case():
# use loop
    while True:
# ask user to input an input with improper casing
        full_name = input("Enter your full name in improper casing:")
        if full_name.strip():
            break
# turn the input to proper cased letters
# print the results 