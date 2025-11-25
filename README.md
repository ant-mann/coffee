# Coffee Machine Simulator ☕

A Python-based command-line interface (CLI) application that simulates the day-to-day operations of a coffee machine. This project was built as part of the Python curriculum on [JetBrains Academy](https://hyperskill.org/).

## 📝 Description

This program creates a virtual coffee machine that manages resources (water, milk, coffee beans, and cups) and finances. It allows users to buy different types of coffee, while allowing the machine operator to restock supplies and withdraw earnings. The program runs on a continuous loop, handling user inputs and checking resource availability before dispensing a drink.

## ✨ Features

* **Drink Selection:** Users can choose from three classic options:
    * **Espresso**
    * **Latte**
    * **Cappuccino**
* **Smart Resource Checking:** The machine calculates if it has enough ingredients before making a coffee. If something is missing (e.g., "Sorry, not enough water!"), it notifies the user without wasting resources.
* **Admin Actions:**
    * `fill`: Add water, milk, coffee beans, and disposable cups to the machine.
    * `take`: Withdraw the money earned from sales.
    * `remaining`: distinct display of current stock levels and cash.
* **Continuous Operation:** The program runs in a main loop allowing multiple actions until the `exit` command is entered.

## 🛠️ Technologies Used

* **Python 3**
* Concepts applied:
    * Input/Output handling
    * `while` loops and control flow
    * Functions and logical conditions
    * String formatting

## 🚀 How to Run

1.  Ensure you have **Python 3.x** installed.
2.  Clone this repository or download the source code.
3.  Navigate to the project directory in your terminal.
4.  Run the script:

    ```bash
    python coffee_machine.py
    ```

## 📋 Usage Example

```text
Write action (buy, fill, take, remaining, exit):
> buy
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money
