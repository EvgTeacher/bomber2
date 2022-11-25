import tkinter as tk

root = tk.Tk()
root.title('My Bomber')
root.geometry("650x650+500+200")
root.resizable(False, False)
root.iconbitmap("bomb.ico")

img_1 = tk.PhotoImage(file="1.gif")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()

root.mainloop()
