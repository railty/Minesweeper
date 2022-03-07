from tkinter import * #brings in all tkinter functionalities of the module
import winsound #winsound modules allows sounds to be played
import random #allows randomization modules and functions
import time #allows time-related functions and delays

def printData():
    for x in range(0,n):
        string = ""
        for y in range(0,n):
            string = string + " " + str(data[x][y])
        print(string)


def printData2():
    for x in range(0,n):
        string = ""
        for y in range(0,n):
            string = string + " " + str(data2[x][y])
        print(string)




#draw a grid with side = h, other side = w and number of lines = n
def gridMaker(n,h,w):
    global gameArea
    for x in range(0,n):
        line = gameArea.create_line(x*w/n,0,x*w/n,w, width = 3)

    for y in range(0,n):
        line = gameArea.create_line(0,y*h/n,h,y*h/n, width = 3)
           
def drawOutlineBox(x,y):
    global gameArea
    global flag
    global flag2
    global flag3
    global bomb

    rectangle = gameArea.create_rectangle(x*width/n,y*height/n,(x+1)*height/n,(y+1)*height/n, width = 4, fill = "light blue", activefill = "lime green")
    
    
    if n == 10:
        if data[y][x] == 8:
            bombMark = gameArea.create_image((x*width/n)+50,(y*height/n)+50, image = bomb, state = HIDDEN)
            print(y, x)
            bombList[y][x] = bombMark
            
    
    
    
    
    if n == 10:
        flagMark = gameArea.create_image((x*width/n)+45,(y*height/n)+48, image = flag, state = HIDDEN)
    elif n == 15:
        flagMark = gameArea.create_image((x*width/n)+35,(y*height/n)+33, image = flag2, state = HIDDEN)
    else: #n == 18:
        flagMark = gameArea.create_image((x*width/n)+28,(y*height/n)+28, image = flag3, state = HIDDEN)
    gameArea.tag_bind(rectangle, '<Button-1>', lambda _: onleftclick(rectangle, x, y))
    gameArea.tag_bind(rectangle, '<Button-3>', lambda _: onrightclick(rectangle, x, y, flagMark))
    gameArea.tag_bind(flagMark, '<Button-3>', lambda _: onrightclickflag(flagMark))




def onleftclick(rectangle, x, y):
    gameArea.itemconfig(rectangle, state = HIDDEN)
    gameArea.update()
    print ("-------")
    playsound()
    #data[y][x] = 1
    
    ct = 0
    if data[y][x] == 8:
        ct = 8
        
    
    else:   
        if y-1>=0 and x-1>=0 and data[y-1][x-1] == 8:
            ct = ct + 1
        if x-1>= 0 and data[y][x-1] == 8:
            ct = ct + 1
        if y+1<n and x-1>= 0 and data[y+1][x-1] == 8:
            ct = ct + 1
        
        if y-1 >= 0 and data[y-1][x] == 8:
            ct = ct + 1
        if y+1 < n and data[y+1][x] == 8:
            ct = ct + 1
            
        if y-1>=0 and x+1<n and data[y-1][x+1] == 8:
            ct = ct + 1
        if x+1 < n and data[y][x+1] == 8:
            ct = ct + 1
        if y+1<n and x+1 <n and data[y+1][x+1] == 8:
            ct = ct + 1
    
    
        
    screenNumber = gameArea.create_text((x*width/n)+50,(y*height/n)+55, text = ct, font = ("courier new", '50'))
    
    if ct == 8:
        screenNumber = gameArea.itemconfig(screenNumber, state = HIDDEN)
    
    
    printData()
    print ('ct = ', ct)

    
    

    if data[y][x] == 8:
        print ("BOMB!")
        print(bombList[y][x])
        gameArea.itemconfig(bombList[y][x], state = NORMAL)

    if data2[y][x] == 0:
        print ("Zero")
        gameArea.itemconfig(screenNumber, state = HIDDEN)
  
def caclAll():
    for x in range(0,n):
        for y in range(0,n):
            data2[y][x] = cacl(x,y)
    printData2()

def cacl(x, y):
    ct = 0
    
    if data[y][x] == 8:
        ct = 8
        return ct
    
    if y-1>=0 and x-1>=0 and data[y-1][x-1] == 8:
        ct = ct + 1
    if x-1>= 0 and data[y][x-1] == 8:
        ct = ct + 1
    if y+1<n and x-1>= 0 and data[y+1][x-1] == 8:
        ct = ct + 1
    
    if y-1 >= 0 and data[y-1][x] == 8:
        ct = ct + 1
    if y+1 < n and data[y+1][x] == 8:
        ct = ct + 1
        
    if y-1>=0 and x+1<n and data[y-1][x+1] == 8:
        ct = ct + 1
    if x+1 < n and data[y][x+1] == 8:
        ct = ct + 1
    if y+1<n and x+1 <n and data[y+1][x+1] == 8:
        ct = ct + 1
        
        
    
    return ct




def placeBombs():
    i = 0
    for x in range(0,n):
        for y in range(0,n):
            data[x][y] = 0
            
    while i < d:
        global bombXvalue
        global bombYvalue
        bombXvalue = random.randint(0,9)
        bombYvalue = random.randint(0,9)
        if data[bombXvalue][bombYvalue] != 8:
            data[bombXvalue][bombYvalue] = 8
            i = i + 1
            
    
    printData()
    print ("-----------")
    

def onrightclick(rectangle, x, y, flagMark):
    gameArea.itemconfig(flagMark, state = NORMAL)
    gameArea.update()
    print ("-------")
    printData()
    
    
    
def onrightclickflag(flagMark):
    gameArea.itemconfig(flagMark, state = HIDDEN)    


def playsound():
    winsound.PlaySound('selectsound', winsound.SND_ASYNC)

def settingsMenu():
    global rootIntro

    initSetting()
    rootIntro.withdraw()

def goBackToIntro():
    global rootSettings
    global rootIntro
    rootIntro.deiconify()
    rootSettings.destroy()

def gameStart():
    global rootIntro
    rootIntro.withdraw()
    initGame()

def initIntro():
    global rootIntro
    introScreen = Canvas(rootIntro, height = 1000, width = 1000, bg = "#4AB586")
    introScreen.pack()

    go = Button(rootIntro, text = "Start Game", height = 1, width = 12, font = ("courier new", '60'), command = gameStart)
    startButton = introScreen.create_window(500, 675, window = go)

    introbg = PhotoImage(file = "introbg.gif")
    introbackground = introScreen.create_image(500,500, image = introbg, state = NORMAL)

    title = introScreen.create_text(500, 350, fill = "#4F0013", text = "MineSweeper", font = ("impact", '80'))
    title2 = introScreen.create_text(495, 345, fill = "white", text = "MineSweeper", font = ("impact", '80'))

    settings = Button(rootIntro, text = "Settings", height = 1, width = 10, font = ("courier new", '15'), command = settingsMenu)
    settingsButton = introScreen.create_window(115, 50, window = settings)

    mainloop()

def initSetting():
    global rootSettings
    rootSettings = Tk()
    settingsScreen = Canvas(rootSettings, height = 1000, width = 1000, bg = "#4AB586")
    goback = Button(rootSettings, text = "Go Back", height = 1, width = 10, font = ("courier new", '15'), command = goBackToIntro)
    goBackButton = settingsScreen.create_window(115, 50, window = goback)
    settingsScreen.pack()
    
def initGame():
    global rootGame
    global gameArea
    global flag
    global flag2
    global flag3
    global bomb
#you cannot create image on Tk(), only Toplevel()
    rootGame = Toplevel()
#creating a canvas
    gameArea = Canvas(rootGame, height = 1000, width = 1000, bg = "tan")
    gameArea.pack() #puts the canvas into the rootGame

    placeBombs()
    caclAll()
    gridMaker(n,height,width)#executes the gridMaker function from before, n is 10, height is 1000 and width is 1000

    for x in range(0,n):
        for y in range(0,n):
            drawOutlineBox(x,y)

    #testrun = Button(root, text = "test", height = 1, width = 12, font = ("courier new", '60'), command = caclAll)
    #testButton = gameArea.create_window(200, 200, window = testrun)

    print(bombList)

    mainloop() #closes the pop-up box. completes it

#variables are stated
width = 1000
height = 1000
n = 10 #number of lines, this can be changed for difficulty
d = 20
firstTimeSettings = 0

bombList = [[0 for x in range(10)] for x in range(10)]


#n = 10, d = 20 is easy mode
#n = 15 is mid mode
#n = 18 is hard mode
   
   
   # for bombs and not bombs, 0 = not bomb, 8 = bomb
data = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],
]

    # for surrounding calculations of nearby bombs, 1-6 is how many bombs are in it's surrounding 3x3 region
data2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],
]

rootIntro = Tk()
rootSettings = None
rootGame = None
gameArea = None

flag = PhotoImage(file = "flag.gif")
flag2 = PhotoImage(file = "flag2.gif")
flag3 = PhotoImage(file = "flag3.gif")
bomb = PhotoImage(file = "bomb.gif")

initIntro()
