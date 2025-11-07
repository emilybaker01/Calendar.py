import tkinter as tk
window = tk.Tk()

def

window.title("My Calendar")
window.geometry("400x300")

label = tk.Label(window, text="Calendar.py", font=("Arial", 14))
label.pack(pady=20)

button =tk.Button(window, text = 'test')
button.pack()

window.mainloop()