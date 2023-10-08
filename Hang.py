import tkinter as tk
from tkinter import messagebox


def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True

    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True

    return False


def check_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True


def on_click(row, col):
    global game_over, turn
    if board[row][col] == "" and not game_over:
        if turn == "X":
            board[row][col] = "X"
            buttons[row][col].config(
                text="X", state="disabled", bg="#ff6f61", fg="white")
            turn_label.config(text="Turn: O", fg="#3caea3")
        else:
            board[row][col] = "O"
            buttons[row][col].config(
                text="O", state="disabled", bg="#3caea3", fg="white")
            turn_label.config(text="Turn: X", fg="#ff6f61")

        if check_winner():
            winner = "O" if turn == "O" else "X"
            messagebox.showinfo("Tic Tac Toe", f"{winner} wins!", icon="info")
            game_over = True
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!", icon="info")
            game_over = True

        if not game_over:
            if turn == "X":
                turn = "O"
            else:
                turn = "X"


def reset_game():
    global game_over, turn
    for row in range(3):
        for col in range(3):
            board[row][col] = ""
            buttons[row][col].config(
                text="", state="active", bg="white", fg="black")
    game_over = False
    turn = "X"
    turn_label.config(text="Turn: X", fg="#ff6f61")


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None, None, None], [None, None, None], [None, None, None]]
turn = "X"
game_over = False

turn_label = tk.Label(root, text="Turn: X", font=(
    "Helvetica", 18, "bold"), fg="#ff6f61", bg="#f0f0f0")
turn_label.pack(pady=(20, 0))

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame, text="", font=("Helvetica", 20, "bold"), width=5, height=2,
                                      command=lambda row=row, col=col: on_click(row, col), bg="white")
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", font=(
    "Helvetica", 14), command=reset_game, fg="white", bg="#3caea3")
reset_button.pack(pady=(20, 0))

root.mainloop()
