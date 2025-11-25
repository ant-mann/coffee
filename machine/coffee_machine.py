class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def print_stock(self):
        print("The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} g of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money")

    def buy(self):
        waterRequired = 0
        milkRequired = 0
        beansRequired = 0
        moneyToAdd = 0
        typeCoffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if typeCoffee == "back":
            return

        if int(typeCoffee) == 1:
            waterRequired = 250
            beansRequired = 16
            moneyToAdd = 4
        elif int(typeCoffee) == 2:
            waterRequired = 350
            milkRequired = 75
            beansRequired = 20
            moneyToAdd = 7
        elif int(typeCoffee) == 3:
            waterRequired = 200
            milkRequired = 100
            beansRequired = 12
            moneyToAdd = 6

        if (self.water >= waterRequired) and (self.milk >= milkRequired) and (self.beans >= beansRequired) and (self.cups > 0):
            self.cups -= 1
            self.water -= waterRequired
            self.milk -= milkRequired
            self.beans -= beansRequired
            self.money += moneyToAdd
            print(f"I have enough resources, making you a coffee!")
        else:
            missingElement = ""
            if self.water < waterRequired:
                missingElement = "water"
            elif self.milk < milkRequired:
                missingElement = "milk"
            elif self.beans < beansRequired:
                missingElement = "coffee beans"
            elif self.cups == 0:
                missingElement = "cups"
            print(f"Sorry, not enough {missingElement}!")

    def action(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            waterToAdd = int(input("Write how many ml of water do you want to add:"))
            milkToAdd = int(input("Write how many ml of milk do you want to add:"))
            beansToAdd = int(input("Write how many grams of coffee beans do you want to add:"))
            cupsToAdd = int(input("Write how many disposable cups of coffee do you want to add:"))
            self.water += waterToAdd
            self.milk += milkToAdd
            self.beans += beansToAdd
            self.cups += cupsToAdd
        elif action == "take":
            print(f"I gave you ${self.money}")
            self.money = 0
        elif action == "remaining":
            self.print_stock()

machine = CoffeeMachine()
leave = False
while not leave:
    userAction = input("Write action (buy, fill, take, remaining, exit):")
    if userAction == "exit":
        leave = True
        break
    machine.action(userAction)