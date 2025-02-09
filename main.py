import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("500x500")

list_of_players = ["X", "0"]

diction_of_winners = {}
diction_of_winners[list_of_players[0]] = 0
diction_of_winners[list_of_players[1]] = 0

MAX_COUNT = 3

buttons = []

current_player = list_of_players[0]

def on_click(row, column):
    global current_player

    if buttons[row][column]['text'] != "":
        return

    buttons[row][column]['text'] = current_player
    if check_winner():
        diction_of_winners[current_player] += 1
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил. Его количество побед: {diction_of_winners[current_player]}")
        if (diction_of_winners[current_player]) == MAX_COUNT:
            messagebox.showinfo("Партия окончена", f"Игрок {current_player} победил в партии")
            for row in buttons:
                for button in row:
                    button.config(state=tk.DISABLED)
            combo_box.config(state=tk.DISABLED)
            reset_button.config(state=tk.DISABLED)
        reset()
        return

    if check_tie():
        messagebox.showinfo(f"Игра окончена", "Ничья")
        return

    current_player = list_of_players[1] if current_player == list_of_players[0] else list_of_players[0]

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
    current_player = combo_box.get()
    for row in buttons:
        for button in row:
            button.config(text="")

def change_choice(event):
    global current_player
    current_player = combo_box.get()

label = tk.Label(window, text="Выберите чем играть:", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=3, pady=10)

combo_box = ttk.Combobox(window, values=list_of_players, state="readonly", font=("Arial", 14))
combo_box.grid(row=1, column=0, columnspan=3, pady=10)
combo_box.set(list_of_players[0])
combo_box.bind("<<ComboboxSelected>>", change_choice)

for i in range(3):
    row = []

    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i + 2, column=j)
        row.append(button)
    buttons.append(row)

reset_button = tk.Button(window, text="Reset", font=("Arial", 20), command=reset)
reset_button.grid(row=6, column=0, columnspan=3, pady=10)


window.mainloop()

