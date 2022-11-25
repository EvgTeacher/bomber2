import tkinter as tk

bomb = 100
score = 0
press_return = True

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
        label.config (text='')
        press_return = False

def update_bomb():
    global bomb
    bomb -=5
    if is_alive():
        fuse_label.after(400, update_bomb)

def click():
    global bomb

def is_alive():
    global bomb
    global press_return
    if bomb <=0:
        bomb = 0
        label.config(text= 'BAM! BAM! BAM! BAM!')
        press_return = True
        return False
    else:
        return True

def update_display():
    global bomb
    global score
    if bomb >= 80:
        bomb_label.config(image= img_1)
    elif bomb >= 50 and bomb < 80:
        bomb_label.config(image=img_2)
    elif bomb > 0 and bomb < 50:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)
    fuse_label.config(text='Fuse: ' + str(bomb))
    score_label.config(text= 'Score: ' + str(score))
    fuse_label.after (100,update_bomb)


root = tk.Tk()
root.title ('bomber')
root.geometry ('1000x1000+100+150')
root.resizable (False,False)

root.iconbitmap('image/bomb.ico')

label = tk.Label(master=root, text='press enter to start' ,
                 font=('fixedsys', 20, 'bold'))
label.pack()


fuse_label =tk.Label(master=root, text=f'Fuse: {str(bomb)}',
                     font=('Courier New', 20, 'bold'))
fuse_label.pack()


score_label = tk.Label(master=root, text=f"Score: {str(score)}",
                       font=('Courier New', 20, 'bold'))
score_label.pack()

img_1 = tk.PhotoImage(file='image/1.gif')
img_2 = tk.PhotoImage(file='image/2.gif')
img_3 = tk.PhotoImage(file='image/3.gif')
img_4 = tk.PhotoImage(file='image/4.gif')


bomb_label = tk.Label(image=img_1)
bomb_label2 = tk.Label(image=img_2)
bomb_label3 = tk.Label(image=img_3)


bomb_label.pack()
bomb_label2.pack()
bomb_label3.pack()

click_button = tk.Button(master=root, text= 'Click me!', bg='black',
                         fg='white', width=15, font=('fixedsys', 20, 'bold'), command=click)

click_button.pack()

root.mainloop()




