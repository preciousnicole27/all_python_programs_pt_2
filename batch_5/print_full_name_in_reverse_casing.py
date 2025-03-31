# define the function that will reverse the casing of the input
def reverse_case():
# use loop
# ask user for input
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
    print("Please input a valid name:")
# turn input into reverse casing
    reverse_cased_name = full_name.swapcase()
# print full name in reverse casing
    print("Reversed Case:", reverse_cased_name)

reverse_case()