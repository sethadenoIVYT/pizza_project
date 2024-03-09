import tkinter as tk
from PIL import ImageTk, Image

# Windows
mainMenu = tk.Tk()

# Titles 
mainMenu.title('Tonys Pizzeria')

# window for carryout orders
def toCarryout():
    # gets size selection from user and prints the price and size
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

    # gets topping selection from user and prints price and topping
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

    # gets sauce selection from user and prints price and sauce
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

    # gets crust selection from user and prints price and crust
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

    # confirms order and disables customization options
    def confirmOrder():

        thankYou = tk.Label(carryOut, text = "Thank You For Your Order. Your Pizza Is Being Made.", font = 'Arial 14 bold')
        sizeButton.config(state = 'disabled')
        toppingButton.config(state = 'disabled')
        sauceButton.config(state = 'disabled')
        crustButton.config(state = 'disabled')
        confirmButton.config(state = 'disabled')
        exitSecond = tk.Button(carryOut, text = "Exit", command = quit) # gives user the option to exit 

        thankYou.grid(row = 21, column = 0)
        exitSecond.grid(row = 22, column = 0)


    # creates carryout window
    carryOut = tk.Tk()
    carryOut.title('Carry Out')
    addOn = format(1.00, ".2f")

    # creates labels for carryout window
    initialGreeting = tk.Label(carryOut, text = " Create Your Pizza ", font = 'Arial 24 bold')
    customSize = tk.Label(carryOut, text = " Select Size: ", font = 'Arial 14 bold')
    customTop = tk.Label(carryOut, text = " Select Topping: ", font = 'Arial 14 bold')
    customSauce = tk.Label(carryOut, text = " Select Sauce: ", font = 'Arial 14 bold')
    customCrust = tk.Label(carryOut, text = " Select Crust: ", font = 'Arial 14 bold')
    priceMessage = tk.Label(carryOut, text = f" Carryout has a base price of ${addOn} plus all prices listed next to selection.", font = 'Arial 14 bold')
    confirmMessage = tk.Label(carryOut, text = " Press Confirm To Order Pizza.", font = 'Arial 14 bold')

    # stores different options for pizza customization
    sizeOptions = ["S", "M", "L"]
    toppingOptions = ["Pepperoni", "Cheese", "Sausage", "Mushroom", "Pepperoni and Sausage", "Sausage and Mushroom", "Pepperoni and Mushroom"]
    sauceOptions = ["Tomato", "Ranch", "BBQ"]
    crustOptions = ["Thin", "Stuffed", "Deep Dish", "Hand Tossed"]

    # initializes selections from user
    selectedSize = tk.StringVar()
    selectedTopping = tk.StringVar()
    selectedSauce = tk.StringVar()
    selectedCrust = tk.StringVar()

    # creates drop down menus for different customization options
    sizeDrop = tk.OptionMenu(carryOut, selectedSize, *sizeOptions)
    topDrop = tk.OptionMenu(carryOut, selectedTopping, *toppingOptions)
    sauceDrop = tk.OptionMenu(carryOut, selectedSauce, *sauceOptions)
    crustDrop = tk.OptionMenu(carryOut, selectedCrust, *crustOptions)

    # creates buttons for confirming customization choices
    sizeButton = tk.Button(carryOut, text = "Confirm Size", command = showSize)
    toppingButton = tk.Button(carryOut, text = "Confirm Topping", command = showTopping)
    sauceButton = tk.Button(carryOut, text = "Confirm Sauce", command = showSauce)
    crustButton = tk.Button(carryOut, text = "Confirm Crust", command = showCrust)
    confirmButton = tk.Button(carryOut, text = "Confirm Order", command = confirmOrder)
   
   # formatting for grid
    initialGreeting.grid(row = 1, column = 0)
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

    priceMessage.grid(row = 18, column = 0)
    confirmMessage.grid(row = 19, column = 0)
    confirmButton.grid(row = 20, column = 0)

    carryOut.mainloop

# window for delivery orders
def toDelivery():
    def showSize():
        # gets size selection from user and prints the price and size
        selected = selectedSize.get()
        if selected == "S":
            sizePrice = 7.00
        elif selected == "M":
            sizePrice = 10.00
        elif selected == "L":
            sizePrice = 13.00

        roundSize = format(sizePrice, ".2f")

        sizeResult.config(text=f"Selected Topping: ${roundSize} {selected}")

    # gets topping selection from user and prints price and topping
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

    # gets sauce selection from user and prints price and sauce
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

    # gets crust selection from user and prints price and crust
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

    # confirms order and disables customization options
    def confirmOrder():

        thankYou = tk.Label(delivery, text = "Thank You For Your Order. Your Pizza Is Being Made.", font = 'Arial 14 bold')
        sizeButton.config(state = 'disabled')
        toppingButton.config(state = 'disabled')
        sauceButton.config(state = 'disabled')
        crustButton.config(state = 'disabled')
        confirmButton.config(state = 'disabled')
        exitSecond = tk.Button(delivery, text = "Exit", command = quit) # gives user the option to exit

        thankYou.grid(row = 21, column = 0)
        exitSecond.grid(row = 22, column = 0)

    # creates delivery window
    delivery = tk.Tk()
    delivery.title('Carry Out')
    addOn = format(7.00, ".2f")

    # creates labels for carryout window
    initialGreeting = tk.Label(delivery, text = " Create Your Pizza ", font = 'Arial 24 bold')
    customSize = tk.Label(delivery, text = " Select Size: ", font = 'Arial 14 bold')
    customTop = tk.Label(delivery, text = " Select Topping: ", font = 'Arial 14 bold')
    customSauce = tk.Label(delivery, text = " Select Sauce: ", font = 'Arial 14 bold')
    customCrust = tk.Label(delivery, text = " Select Crust: ", font = 'Arial 14 bold')
    priceMessage = tk.Label(delivery, text = f" Delivery has a base price of ${addOn} plus all prices listed next to selection.", font = 'Arial 14 bold')
    confirmMessage = tk.Label(delivery, text = " Press Confirm To Order Pizza.", font = 'Arial 14 bold')

    # stores different options for pizza customization
    sizeOptions = ["S", "M", "L"]
    toppingOptions = ["Pepperoni", "Cheese", "Sausage", "Mushroom", "Pepperoni and Sausage", "Sausage and Mushroom", "Pepperoni and Mushroom"]
    sauceOptions = ["Tomato", "Ranch", "BBQ"]
    crustOptions = ["Thin", "Stuffed", "Deep Dish", "Hand Tossed"]

    # initializes selections from user
    selectedSize = tk.StringVar()
    selectedTopping = tk.StringVar()
    selectedSauce = tk.StringVar()
    selectedCrust = tk.StringVar()

    # creates drop down menus for different customization options
    sizeDrop = tk.OptionMenu(delivery, selectedSize, *sizeOptions)
    topDrop = tk.OptionMenu(delivery, selectedTopping, *toppingOptions)
    sauceDrop = tk.OptionMenu(delivery, selectedSauce, *sauceOptions)
    crustDrop = tk.OptionMenu(delivery, selectedCrust, *crustOptions)

    # creates buttons for confirming customization choices
    sizeButton = tk.Button(delivery, text = "Confirm Size", command = showSize)
    toppingButton = tk.Button(delivery, text = "Confirm Topping", command = showTopping)
    sauceButton = tk.Button(delivery, text = "Confirm Sauce", command = showSauce)
    crustButton = tk.Button(delivery, text = "Confirm Crust", command = showCrust)
    confirmButton = tk.Button(delivery, text = "Confirm Order", command = confirmOrder)
   
   # formatting for grid 
    initialGreeting.grid(row = 1, column = 0)
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

    sizeResult = tk.Label(delivery, text="")
    sizeResult.grid(row = 5, column = 0)

    toppingResult = tk.Label(delivery, text="")
    toppingResult.grid(row = 9, column = 0)

    sauceResult = tk.Label(delivery, text="")
    sauceResult.grid(row = 13, column = 0)

    crustResult = tk.Label(delivery, text="")
    crustResult.grid(row = 17, column = 0)

    priceMessage.grid(row = 18, column = 0)
    confirmMessage.grid(row = 19, column = 0)
    confirmButton.grid(row = 20, column = 0)

    delivery.mainloop

# Images
greetingImage = Image.open("GreetingMenuImage.jpg")
resize_greetingImage = greetingImage.resize((225, 150))
finalImage = ImageTk.PhotoImage(resize_greetingImage)

hoursImage = Image.open("hours.jpg")
resize_hoursImage = hoursImage.resize((225, 150))
finalHoursImage = ImageTk.PhotoImage(resize_hoursImage)

# Labels
greeting1 = tk.Label(mainMenu, text = ' Welcome to the Tonys Pizzeria Ordering Service!', font='Arial 24 bold')
greeting2 = tk.Label(mainMenu, text = ' How Can We Assist You Today?', font = 'Arial 24 bold')
greetingImageLabel = tk.Label(mainMenu, image = finalImage)
hoursImageLabel = tk.Label(mainMenu, image = finalHoursImage)

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
hoursImageLabel.grid(row = 6, column = 0)

mainMenu.mainloop()
