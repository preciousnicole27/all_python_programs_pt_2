# define the function that will convert the number to 6 digits with leading zeroes
def six_digit_format():
# use a while True loop and try 
    while True:
        try:
# ask for user input
            number = int(input("Enter a number from 0-1000:"))
            if 0 <= number <= 1000:
                break
            print("Number out of range")
        except ValueError:
            print("Invalid input, Enter a new number:")
# format the number to 6 digits with leading zero
    formatted_number = f"{number:06}"
# print the number in six digit format
    print("Output:", formatted_number)
    
six_digit_format()