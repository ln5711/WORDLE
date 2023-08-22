import tkinter as tk

def process_input(event):
    global user_input
    user_input = myentry.get()
    myentry.delete(0, tk.END)

root = tk.Tk()

root.geometry("500x500")
root.title("WORDLE")

label = tk.Label(root, text="WORDLE", font=('Arial', 30))
label.pack(padx=20, pady=20)

myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

myentry.bind("<Return>", process_input)
root.geometry("500x500")

label.pack(padx=20, pady=20)

# Create a frame for the grid of text boxes
frame = tk.Frame(root)
frame.pack(pady=20)  # Add padding around the frame for aesthetics

# Create a 5x6 grid of text boxes within the frame
labels = [[tk.Label(frame, width=10,height=5,text="" , borderwidth=2, relief="solid") for j in range(5)] for i in range(6)]
for i in range(6):
    for j in range(5):
        labels[i][j].grid(row=i, column=j, padx=5, pady=5)
root.mainloop()
