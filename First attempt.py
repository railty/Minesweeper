from tkinter import * #brings in all tkinter functionalities of the module

root = Tk() #creates a pop-up called "root" to put out GUI

#creating a canvas
gameArea = Canvas(root, height = 1200, width = 1200, bg = "tan")
gameArea.pack() #puts the canvas into the root

num1 = gameArea.create_text(200, 200, text = "0", font = ("courier new", '24'))
num2 = gameArea.create_text(400, 200, text = "0", font = ("courier new", '24'))
num3 = gameArea.create_text(600, 200, text = "0", font = ("courier new", '24'))
num4 = gameArea.create_text(800, 200, text = "0", font = ("courier new", '24'))
num5 = gameArea.create_text(1000, 200, text = "0", font = ("courier new", '24'))
num6 = gameArea.create_text(200, 400, text = "0", font = ("courier new", '24'))
num7 = gameArea.create_text(400, 400, text = "0", font = ("courier new", '24'))
num8 = gameArea.create_text(600, 400, text = "0", font = ("courier new", '24'))
num9 = gameArea.create_text(800, 400, text = "0", font = ("courier new", '24'))
num10 = gameArea.create_text(1000, 400, text = "0", font = ("courier new", '24'))
num11 = gameArea.create_text(200, 600, text = "0", font = ("courier new", '24'))
num12 = gameArea.create_text(400, 600, text = "0", font = ("courier new", '24'))
num13 = gameArea.create_text(600, 600, text = "0", font = ("courier new", '24'))
num14 = gameArea.create_text(800, 600, text = "0", font = ("courier new", '24'))
num15 = gameArea.create_text(1000, 600, text = "0", font = ("courier new", '24'))
num16 = gameArea.create_text(200, 800, text = "0", font = ("courier new", '24'))
num17 = gameArea.create_text(400, 800, text = "0", font = ("courier new", '24'))
num18 = gameArea.create_text(600, 800, text = "0", font = ("courier new", '24'))
num19 = gameArea.create_text(800, 800, text = "0", font = ("courier new", '24'))
num20 = gameArea.create_text(1000, 800, text = "0", font = ("courier new", '24'))
num21 = gameArea.create_text(200, 1000, text = "0", font = ("courier new", '24'))
num22 = gameArea.create_text(400, 1000, text = "0", font = ("courier new", '24'))
num23 = gameArea.create_text(600, 1000, text = "0", font = ("courier new", '24'))
num24 = gameArea.create_text(800, 1000, text = "0", font = ("courier new", '24'))
num25 = gameArea.create_text(1000, 1000, text = "0", font = ("courier new", '24'))
mainloop() #closes the pop-up box. completes it.