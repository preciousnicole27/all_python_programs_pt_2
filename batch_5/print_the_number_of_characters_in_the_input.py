# define the function that will count the number of characters in the input
def count_characters():
# use loop
# ask user for input
    while True:
        full_name = ("Enter your full name:")
        if full_name.strip():
            break
        else:
            print("Please input a valid name:")
# count the number of characters un the input
    character_count = len(full_name.replace(" ",""))
# print the number of characters

count_characters()