import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("my first GUI")

label = tk.Label(root, text="Hello world!", font=("Arial", 18))
label.pack(padx=20, pady=20)

# myentry = tk.Entry(root)
# myentry.pack()

textbox = tk.Text(root, height=5,  font=("Arial", 18))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text=1, font=("Arial", 18))
btn1.grid(row=0, column=0, sticky='ew')

btn2 = tk.Button(buttonframe, text=2, font=("Arial", 18))
btn2.grid(row=0, column=1, sticky='ew')

btn3 = tk.Button(buttonframe, text=3, font=("Arial", 18))
btn3.grid(row=0, column=2, sticky='ew')

btn4 = tk.Button(buttonframe, text=4, font=("Arial", 18))
btn4.grid(row=1, column=0, sticky='ew')

btn5 = tk.Button(buttonframe, text=5, font=("Aial", 18))
btn5.grid(row=1, column=1, sticky='ew')

btn6 = tk.Button(buttonframe, text=6, font=("Arial", 18))
btn6.grid(row=1, column=2, sticky='ew')

buttonframe.pack(fill="x")

anotherbtn = tk.Button(root, text="TEST", fg="green")
anotherbtn.place(x=200, y=400, height=100, width=100)
# button = tk.Button(root, text="click me!", font=("Arial", 18))
# button.pack(padx=10, pady=10)

root.mainloop()
