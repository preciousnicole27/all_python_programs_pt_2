# define the function that will convert improper casing to pascal casing
def pascal_case():
# use loop
    while True:
# ask for user input in incorrect casing
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
    else:
        print("Please put a valid input:")
# turn input into pascal casing
    pascal_case_name = full_name.title().replace(" ", "")
# print the results
    print("Output:", pascal_case_name)
pascal_case()