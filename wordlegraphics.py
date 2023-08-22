import tkinter as tk

def process_input(event):
    word = myentry.get()
    for i in range(len(word)):
        update_specific_label(0, i, word[i],int)
    myentry.delete(0, tk.END) # deletes the entry once its entered

def update_specific_label(row, column, char,info):
    specific_label = labels[row][column]

    if info == 0:
        specific_label.config(text=char,fg="white", font=('Arial', 15, "bold"), background="green")
    elif info == 1:
        specific_label.config(text=char,fg="white", font=('Arial', 15, "bold"), background="yellow")
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

myentry.bind("<Return>", process_input)
root.geometry("500x500")
label.pack(padx=20, pady=20)
root.mainloop()
