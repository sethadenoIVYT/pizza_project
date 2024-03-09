import tkinter as tk
from PIL import ImageTk, Image

# Windows
mainMenu = tk.Tk()

# Titles 
mainMenu.title('Tonys Pizzeria')

def toCarryout():
    def showSize():
        selected = selectedSize.get()
        if selected == "S":
            sizePrice = 7.00
        elif selected == "M":
            sizePrice = 10.00
        elif selected == "L":
            sizePrice = 13.00

        roundSize = format(sizePrice, ".2f")

        sizeResult.config(text=f"Selected Topping: ${roundSize} {selected}")

    def showTopping():
        selected = selectedTopping.get()
        if selected == "Pepperoni":
            topPrice = 2.00
        elif selected == "Cheese":
            topPrice = 1.00
        elif selected == "Sausage":
            topPrice = 2.00
        elif selected == "Mushroom":
            topPrice = 2.00
        elif selected == "Pepperoni and Sausage":
            topPrice = 4.00
        elif selected == "Sausage and Mushroom":
            topPrice = 4.00
        elif selected == "Pepperoni and Mushroom":
            topPrice = 4.00

        roundTop = format(topPrice, ".2f")

        toppingResult.config(text=f"Selected Topping: ${roundTop} {selected}")

    def showSauce():
        selected = selectedSauce.get()
        if selected == "Tomato":
            saucePrice = 1.00
        elif selected == "Ranch":
            saucePrice = 2.00
        elif selected == "BBQ":
            saucePrice = 2.00

        roundSauce = format(saucePrice, ".2f")

        sauceResult.config(text=f"Selected Topping: ${roundSauce} {selected}")

    def showCrust():
        selected = selectedCrust.get()
        if selected == "Thin":
            crustPrice = 1.00
        elif selected == "Stuffed":
            crustPrice = 5.00
        elif selected == "Deep Dish":
            crustPrice = 3.00
        elif selected == "Hand Tossed":
            crustPrice = 1.00


        roundCrust = format(crustPrice, ".2f")

        crustResult.config(text=f"Selected Topping: ${roundCrust} {selected}")

    carryOut = tk.Tk()
    carryOut.title('Carry Out')
    addOn = 1.00

    customImage = Image.open("createPizza.jpg")
    resize_customImage = customImage.resize((225, 150))
    finalCustomImage = ImageTk.PhotoImage(resize_customImage)
    
    initialGreeting = tk.Label(carryOut, text = " Create Your Pizza ", font = 'Arial 24 bold')
    customImageLabel = tk.Label(carryOut, image = finalCustomImage)
    customSize = tk.Label(carryOut, text = " Select Size: ", font = 'Arial 14 bold')
    customTop = tk.Label(carryOut, text = " Select Topping: ", font = 'Arial 14 bold')
    customSauce = tk.Label(carryOut, text = " Select Sauce: ", font = 'Arial 14 bold')
    customCrust = tk.Label(carryOut, text = " Select Crust: ", font = 'Arial 14 bold')

    sizeOptions = ["S", "M", "L"]
    toppingOptions = ["Pepperoni", "Cheese", "Sausage", "Mushroom", "Pepperoni and Sausage", "Sausage and Mushroom", "Pepperoni and Mushroom"]
    sauceOptions = ["Tomato", "Ranch", "BBQ"]
    crustOptions = ["Thin", "Stuffed", "Deep Dish", "Hand Tossed"]

    selectedSize = tk.StringVar()
    selectedTopping = tk.StringVar()
    selectedSauce = tk.StringVar()
    selectedCrust = tk.StringVar()

    sizeDrop = tk.OptionMenu(carryOut, selectedSize, *sizeOptions)
    topDrop = tk.OptionMenu(carryOut, selectedTopping, *toppingOptions)
    sauceDrop = tk.OptionMenu(carryOut, selectedSauce, *sauceOptions)
    crustDrop = tk.OptionMenu(carryOut, selectedCrust, *crustOptions)

    sizeButton = tk.Button(carryOut, text = "Confirm Size", command = showSize)
    toppingButton = tk.Button(carryOut, text = "Confirm Topping", command = showTopping)
    sauceButton = tk.Button(carryOut, text = "Confirm Sauce", command = showSauce)
    crustButton = tk.Button(carryOut, text = "Confirm Crust", command = showCrust)
   
    initialGreeting.grid(row = 0, column = 0)
    customImageLabel.grid(row = 1, column = 0)

    customSize.grid(row = 2, column = 0)
    sizeDrop.grid(row = 3, column = 0)
    sizeButton.grid(row = 4, column = 0)

    customTop.grid(row = 6, column = 0)
    topDrop.grid(row = 7, column = 0)
    toppingButton.grid(row = 8, column = 0)

    customSauce.grid(row = 10, column = 0)
    sauceDrop.grid(row = 11, column = 0)
    sauceButton.grid(row = 12, column = 0)

    customCrust.grid(row = 14, column = 0)
    crustDrop.grid(row = 15, column = 0)
    crustButton.grid(row = 16, column = 0)

    sizeResult = tk.Label(carryOut, text="")
    sizeResult.grid(row = 5, column = 0)

    toppingResult = tk.Label(carryOut, text="")
    toppingResult.grid(row = 9, column = 0)

    sauceResult = tk.Label(carryOut, text="")
    sauceResult.grid(row = 13, column = 0)

    crustResult = tk.Label(carryOut, text="")
    crustResult.grid(row = 17, column = 0)

    carryOut.mainloop

def toDelivery():
    testWin2 = tk.Tk()
    addOn = 7.00
    testCost = tk.Label(testWin2, text = addOn)
    testCost.grid(row = 0, column = 0)
    testWin2.mainloop

# Images
greetingImage = Image.open("GreetingMenuImage.jpg")
resize_greetingImage = greetingImage.resize((225, 150))
finalImage = ImageTk.PhotoImage(resize_greetingImage)

# Labels
greeting1 = tk.Label(mainMenu, text = ' Welcome to the Tonys Pizzeria Ordering Service!', font='Arial 24 bold')
greeting2 = tk.Label(mainMenu, text = ' How Can We Assist You Today?', font = 'Arial 24 bold')
greetingImageLabel = tk.Label(mainMenu, image = finalImage)

# Buttons
carryOutButton = tk.Button(mainMenu, text = "Carry Out", height = 2, width = 8, command = toCarryout)
deliveryButton = tk.Button(mainMenu, text = "Delivery", height = 2, width = 8, command = toDelivery)
exitButton = tk.Button(mainMenu, text = "Exit", height = 2, width = 8, command = mainMenu.quit)

# Grid Placement 
greeting1.grid(row = 0, column = 0)
greeting2.grid(row = 1, column = 0)
greetingImageLabel.grid(row = 2, column = 0)
carryOutButton.grid(row = 3, column = 0)
deliveryButton.grid(row = 4, column = 0)
exitButton.grid(row = 5, column = 0)

mainMenu.mainloop()
