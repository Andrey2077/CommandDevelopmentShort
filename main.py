import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("500x300")

current_player = "X"
buttons = []

def on_click(row, column):
    global current_player

    if buttons[row][column]['text'] != "":
        return


    buttons[row][column]['text'] = current_player
    if check_winner():
        messagebox.showinfo(f"Игра окончена",  f"Игрок {current_player} победил")
        return


    if check_tie():
        messagebox.showinfo(f"Игра окончена", "Ничья")
        return


    current_player = "0" if current_player == "X" else "X"

def check_tie():

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False

    return True


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def reset():
    global current_player
    current_player = "X"
    for row in buttons:
        for button in row:
            button.config(text="")


for i in range(3):
    row = []

    for j in range(3):
        button = tk.Button(window, text="", font= ("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

reset_button = tk.Button(window, text="Reset", font=("Arial", 20), command=reset)
reset_button.grid(row=0, column=3, columnspan=3, padx=10)


window.mainloop()

