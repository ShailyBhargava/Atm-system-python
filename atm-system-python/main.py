class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited. Your updated balance is: ${self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} has been withdrawn. Your updated balance is: ${self.balance}")
        else:
            print("Invalid amount or insufficient funds")

def main():
    atm = ATM()
    while True:
        print("\nWelcome To ATM Machine")
        print("1. Check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. exit")
        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue
        
        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == 4:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
