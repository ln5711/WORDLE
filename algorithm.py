import csv
import random

def read_csv():
    words = []
    with open('5_letter_words.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            words.append(row[0])
    return words


def save_info(word):
    letter_counts = {}
    # Loop through each letter in the word
    for letter in word:
        # If the letter is already in the dictionary, increment its count by 1
        if letter in letter_counts:
            letter_counts[letter] += 1
        # If the letter is not in the dictionary, add it with a count of 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def input_word(word_list):
    while True:
        user_input = input("Please enter a five letter word:"'\n').strip()
        if user_input in word_list:
            break
        else:
            print("thats not a five letter word" '\n')
    return user_input

def compare(g,winfo,w): #tells us each correct character tells incorrect characters
                                    #tells correct character in correct position and vice versa
                                    #0 is right char right position 1 right char wrong pos  2 is neither
    info = [2] * 5
    if g == w: #checks if you guessed the right word
        for index in info:
            info[index] = 0
        return info
    for letter, count in winfo.items():
        iterator = 0
        count2 = 0
        for index in g:
            if letter == g[iterator]:  #if it has letter
                #we check to see if its the right position
                if w[iterator] == g[iterator]: #index is loop count
                    info[iterator] = 0  #sets inex to correct
                    print(letter + " at index " + str(iterator) + " is at right posiiton")
                    count2 +=1
                else:
                    info[iterator] = 1
                    print(letter + " at index " + str(iterator) + " is right but wrong position")
                    count2 +=1
                if count == count2:
                    break
            iterator += 1
    return info















#word_list = read_csv() #reads csv and puts in list
#index = random.randint(0,495) #chooses index randomly for word
#word_info = save_info(word_list[index]) #saves information of specific word amounts of letter
#counter = 0
#print(word_list[index])
#while counter < 6:
#    guess = input_word() #make lowercase
#    result = compare(guess,word_info,word_list[index])
#   if result:
#        print("correct")
#        break
#    else:
#        print("try again")
#    counter +=1
#print(word_list[index])
###

