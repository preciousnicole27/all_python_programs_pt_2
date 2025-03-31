# define the function that will count the number of words in an input
def count_words():
# use loop
# ask user for input
    while True:
        sentence = input("Enter a sentence:")
        if sentence.strip():
            break
    print("Please enter a valid sentence:") 
# count the number of words in the input
    word_count = len(sentence.split())
# print the amount of words 
    print("Number of words:", word_count)
count_words()