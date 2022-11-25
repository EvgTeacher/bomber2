import tkinter as tk


def start(event):
    global press_return
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        update_bomb()
        update_score()
        update_display()
        label.config(text='')
        press_return = False
def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)

def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        bomb = 0
        label.config(text="BANG! BANG! BANG! BANG!")
        press_return = True
        return False
    else:
        return True

def update_display():
    global bomb
    global score
    if bomb >= 80:
        bomb_label.config(image=img_1)
    elif bomb >= 50 and bomb < 80:
        bomb_label.config(image=img_2)
    elif bomb > 0 and bomb < 50:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)
    fuse_label.config(text='Fuse: ' + str(bomb))
    score_label.config(text="Score " + str(score))
    fuse_label.after(100, update_bomb)


def click():
    global bomb



bomb = 100
score = 0
press_return = True

root = tk.Tk()
root.title('My Bomber')
root.geometry("650x650+500+200")
root.resizable(False, False)
# root.minsize(200, 200)
# root.maxsize(700, 700)
root.iconbitmap("image/bomb.ico")

label = tk.Label(master=root, text="Press [enter] to start the game",
                 font=("Comic Sans MS", 14, "bold"))
label.pack()

fuse_label = tk.Label(master=root, text=f"Fuse: {str(bomb)}",
                            font=("Comic Sans MS", 14, "bold"))
fuse_label.pack()
score_label = tk.Label(master=root, text=f"Score: {str(score)}",
                       font=("Comic Sans MS", 14, "bold"))
score_label.pack()

img_1 = tk.PhotoImage(file="image/1.gif")
img_2 = tk.PhotoImage(file="image/2.gif")
img_3 = tk.PhotoImage(file="image/3.gif")
img_4 = tk.PhotoImage(file="image/4.gif")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()

click_button = tk.Button(master=root, text="Click me", bg="black",
                         fg='white', width=15, font=("Comic Sans MS", 14, "bold"), command=click)
click_button.pack()

root.mainloop()








