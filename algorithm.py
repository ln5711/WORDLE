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
    #loop through each letter in the word
    for letter in word:
        #if the letter is already in the dictionary, increment its count by 1
        if letter in letter_counts:
            letter_counts[letter] += 1
        #if the letter is not in the dictionary, add it with a count of 1
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


def compare(g, winfo, w):
    info = [2] * 5
    guess_letter_counts = save_info(g) #get letter counts for the guess

    #check for correct position
    for index in range(len(g)):
        if g[index] == w[index]:
            info[index] = 0
            if guess_letter_counts[g[index]] > 0:
                guess_letter_counts[g[index]] -= 1 #deduct a count from the guess
            if winfo[g[index]] > 0:
                winfo[g[index]] -= 1 #deduct a count from the word

    #check if the letter exists anywhere in the word
    for index, letter in enumerate(g):
        if info[index] != 0 and letter in winfo and guess_letter_counts[letter] > 0 and winfo[letter] > 0:
            info[index] = 1
            guess_letter_counts[letter] -= 1
            winfo[letter] -= 1

    return info
#

    #for index, letter in enumerate(g):  # Using enumerate to get index and letter
        #if letter in winfo:  # if it has the letter
         #   if w[index] == letter:  # check if it's the right position
           #     info[index] = 0
           # else:
          #      info[index] = 1

  #  return info

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
