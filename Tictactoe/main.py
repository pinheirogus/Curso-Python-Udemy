from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Gus' TicTacToe")

# Reset the game

def reset():
    pass

# Keeping track of turns
class Turn:
    def __init__(self):
        self.x_turn = True
        self.counter = 0

turn_tracker = Turn()

# Disabling buttons when there's a winner

def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)


# Check to see if someone won

def checkForWinner():
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        winner = True
    if b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        winner = True
    if b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        winner = True
    if b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        winner = True
    if b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        winner = True
    if b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        winner = True
    if b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        winner = True
    if b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        winner = True

    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        winner = True
    if b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        winner = True
    if b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        winner = True
    if b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        winner = True
    if b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        winner = True
    if b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        winner = True
    if b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        winner = True
    if b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        winner = True
    if winner == True:
        disable_all_buttons()
    return winner

# Function button clicked
def btn_click(b):
    if b["text"] == " " and turn_tracker.x_turn == True:
        b["text"] = "X"
        turn_tracker.x_turn = False
        turn_tracker.counter += 1
        if checkForWinner():
            messagebox.showinfo("Tic Tac Toe", "X Wins!")
        return b
    elif b["text"] == " " and turn_tracker.x_turn == False:
        b["text"] = "O"
        turn_tracker.x_turn = True
        turn_tracker.counter += 1
        if checkForWinner():
            messagebox.showinfo("Tic Tac Toe", "O Wins!")
        return b
    else:
        messagebox.showerror("Tic Tac Toe", "That space is already taken, pick another.")
        # pass

# Building buttons

b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b2 ))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b4, ))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b5, ))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b6, ))
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b7, ))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b8, ))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_click(b9, ))

#Creating grid for the buttons

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# Create menu

main_menu = Menu(root)
root.config(menu=main_menu)

# Create options Menu
options_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset())


# if __name__ == '__main__':
#     print_hi('PyCharm')

root.mainloop()
