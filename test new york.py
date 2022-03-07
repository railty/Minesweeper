from tkinter import * #brings in all tkinter functionalities of the module
root = Tk()

def settingsMenu():
    global root
    root.destroy()
    root = Tk()
    settingsScreen = Canvas(root, height = 1000, width = 1000, bg = "#4AB586")
    settingsScreen.pack()
    mainloop()

introScreen = Canvas(root, height = 1000, width = 1000, bg = "#4AB586")
introScreen.pack()

settings = Button(root, text = "Settings", height = 1, width = 10, font = ("courier new", '15'), command = settingsMenu)
settingsButton = introScreen.create_window(115, 50, window = settings)


mainloop()

