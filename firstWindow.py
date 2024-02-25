import tkinter as tk
from PIL import ImageTk, Image

# Windows
mainMenu = tk.Tk()

# Titles 
mainMenu.title('Tonys Pizzeria')

# Window Geometry 
mainMenu.geometry('575x400')
mainMenu.resizable(False, False)

# opens new window that will be for placing orders
def toOrder():
    testWin = tk.Tk()
    testWin.mainloop

# Images
greetingImage = Image.open("GreetingMenuImage.jpg")
resize_greetingImage = greetingImage.resize((225, 150))
finalImage = ImageTk.PhotoImage(resize_greetingImage)

# Labels
greeting1 = tk.Label(mainMenu, text = ' Welcome to the Tonys Pizzeria Ordering Service!', font='Arial 24 bold')
greeting2 = tk.Label(mainMenu, text = ' How Can We Assist You Today?', font = 'Arial 24 bold')
greetingImageLabel = tk.Label(mainMenu, image = finalImage)

# Buttons
carryOutButton = tk.Button(mainMenu, text = "Carry Out", height = 2, width = 8, command = toOrder)
deliveryButton = tk.Button(mainMenu, text = "Delivery", height = 2, width = 8, command = toOrder)
exitButton = tk.Button(mainMenu, text = "Exit", height = 2, width = 8, command = mainMenu.quit)

# Grid Placement 
greeting1.grid(row = 0, column = 0)
greeting2.grid(row = 1, column = 0)
greetingImageLabel.grid(row = 2, column = 0)
carryOutButton.grid(row = 3, column = 0)
deliveryButton.grid(row = 4, column = 0)
exitButton.grid(row = 5, column = 0)

mainMenu.mainloop()
