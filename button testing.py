import tkinter as tk

def onclick():
    print("Button Clicked")
    
root = tk.Tk()
root.title("GUI BUTTON")

btn1 = tk.Button(root, text = "Button 1", command=onclick)
btn2 = tk.Button(root, text = "Button 1", command=onclick)


btn1.pack()
btn2.pack()

root.mainloop()