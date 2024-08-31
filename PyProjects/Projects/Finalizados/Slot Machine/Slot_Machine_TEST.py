import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROW = 3
COL = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
          all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    print(columns)
    return columns
    

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
def deposit():
    while True:
        amount = input("how much would you like to deposit?. $")
        if amount.isdigit():
            amount = int(amount)
            if amount  > 0:
                break
            else:
                print("your deposit must be greater than 0.")
        else:
            print("you must deposit a valid number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
                      "how many lines would you like to bet on (1- " +str(MAX_LINES) + ")?. ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("choose a valid number of lines.")
        else:
            print("you must choose a valid number.")

    return lines

def get_bet():
    while True:
        amount = input("How much money would you like to bet on each line?. $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("your bet must be a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

        print(f"you are betting ${bet} on {lines}. Total bet is equal to ${total_bet}")
    slots = get_machine_spin(ROW, COL, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won $ {winnings}.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"your balance is ${balance}")
        answer= input("press enter to play / q to quit")
        if answer == "q":
            break
        else:
            balance += spin(balance)

    print(f"you left with $ {balance}")
    
main()