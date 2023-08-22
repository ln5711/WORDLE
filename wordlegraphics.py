import tkinter as tk
import random
import csv
from algorithm import *
global counter
counter = 0

def process_input(event):
    global counter
    guess = myentry.get()
    info = compare(guess,word_info,word_list[index])  #make it so compare will give info on each char editing i for each
    for i in range(len(guess)):
        update_specific_label(counter, i, guess[i],info)
    myentry.delete(0, tk.END) # deletes the entry once its entered
    counter += 1

def update_specific_label(row, column, char,info):
    specific_label = labels[row][column]
    char = char.upper()
    if info[column] == 0:
        specific_label.config(text=char,fg="white", font=('Arial', 15, "bold"), background="green")
    elif info[column] == 1:
        specific_label.config(text=char,fg="white", font=('Arial', 15, "bold"), background="#ffc425")
    else:
        specific_label.config(text=char,fg="white", font=('Arial', 15, "bold"), background="grey")

root = tk.Tk()

root.geometry("1000x1000")
root.title("WORDLE")

label = tk.Label(root, text="WORDLE", font=('Arial', 50, "bold"))
label.pack(padx=20, pady=20)

myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

# Create a frame for the grid of text boxes
frame = tk.Frame(root)
frame.pack(pady=20)  # Add padding around the frame

# Create a 5x6 grid of text boxes within the frame
labels = [[tk.Label(frame, width=10, height=5, borderwidth=2, relief="solid") for j in range(5)] for i in range(6)]
for i in range(6):
    for j in range(5):
        labels[i][j].grid(row=i, column=j, padx=5, pady=5)

#myentry.bind("<Return>", process_input)
root.geometry("500x500")
label.pack(padx=20, pady=20)


word_list = read_csv() #reads csv and puts in list
index = random.randint(0,495) #chooses index randomly for word
word_info = save_info(word_list[index]) #saves information of specific word amounts of letter
print(word_list[index])
myentry.bind("<Return>", process_input)
while counter < 6:
    root.update_idletasks()
    root.update()
print(word_list[index])

root.mainloop()
