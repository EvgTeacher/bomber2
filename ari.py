import tkinter as tk
root = tk.Tk()
root.title('Ari&Falba')
root.geometry("1200x1200")
root.resizable(False, False)
img1 = tk.PhotoImage(file="1.gif")
img2 = tk.PhotoImage(file="2.gif")
img1_label = tk.Label(image=img1)
img1_label.pack()
img2_label = tk.Label(image=img2)
img2_label.pack()


root.mainloop()