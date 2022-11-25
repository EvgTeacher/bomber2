import tkinter as tk

root = tk.Tk()
root.geometry("1250x720")
root.title('home work')

img = tk.PhotoImage(file="image/1.gif")
img2 = tk.PhotoImage(file="image/2.gif")
img3 = tk.PhotoImage(file="image/3.gif")

l = tk.Label()
l.pack()

x = 1
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    x = x + 1
    root.after(2000, move)


move()

root.mainloop()