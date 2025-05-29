from tkinter import *
from PIL import Image, ImageTk
from random import choice

root = Tk()
root.title("Rock Paper Scissors")
root.config(bg="light blue")
root.geometry("600x400")



comp_images = {
    "rock": ImageTk.PhotoImage(Image.open("rock.png")),
    "paper": ImageTk.PhotoImage(Image.open("paper.png")),
    "scissor": ImageTk.PhotoImage(Image.open("scissors.png"))
}


user_label = Label(root, image=user_images["scissor"], bg="light blue")
comp_label = Label(root, image=comp_images["scissor"], bg="light blue")
user_label.grid(row=1, column=4)
comp_label.grid(row=1, column=0)

player_score = Label(root, text="0", font=("Arial", 20), fg="red", bg="light blue")
computer_score = Label(root, text="0", font=("Arial", 20), fg="red", bg="light blue")
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

Label(root, text="USER", font=20, bg="black", fg="red").grid(row=0, column=3)
Label(root, text="COMPUTER", font=20, bg="black", fg="red").grid(row=0, column=1)
msg = Label(root, text="", font=20, bg="red", fg="white")
msg.grid(row=3, column=2)


def update_result(text):
    msg.config(text=text)

def update_user_score():
    score = int(player_score["text"]) + 1
    player_score.config(text=str(score))

def update_comp_score():
    score = int(computer_score["text"]) + 1
    computer_score.config(text=str(score))


def decide_winner(user, comp):
    if user == comp:
        update_result("It's a Tie!")
    elif (user == "rock" and comp == "scissor") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"):
        update_result("You Win!")
        update_user_score()
    else:
        update_result("You Lose!")
        update_comp_score()


def make_choice(user_choice):
    comp_choice = choice(["rock", "paper", "scissor"])
    user_label.config(image=user_images[user_choice])
    comp_label.config(image=comp_images[comp_choice])
    decide_winner(user_choice, comp_choice)


Button(root, text="ROCK", width=15, height=2, bg="red", fg="white", command=lambda: make_choice("rock")).grid(row=2, column=1)
Button(root, text="PAPER", width=15, height=2, bg="green", fg="white", command=lambda: make_choice("paper")).grid(row=2, column=2)
Button(root, text="SCISSOR", width=15, height=2, bg="blue", fg="white", command=lambda: make_choice("scissor")).grid(row=2, column=3)

root.mainloop()
