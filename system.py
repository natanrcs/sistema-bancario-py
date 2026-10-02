class Account:
    def __init__(self, account_owner: str, account_number: str, bank_name: str, agency: str):
        self.account_owner = account_owner
        self.account_number = account_number
        self.bank_name = bank_name
        self.agency = agency
        self.balance = 0.0
        self.extract = []

    def deposit(self, value: float):
        if value <= 0:
            return "Deposit declined."
        else:
            self.balance += value
            data = {"type": "deposit","value": value}
            self.extract.append(data)
            return f"Deposit completed. current balance: {self.balance}"

    def withdraw(self, value: float):
        if value <= 0:
            return "Withdrawal denied."
        elif value > self.balance:
            return "insufficient funds."
        else:
            self.balance -= value
            data = {"type": "withdrawal","value": value}
            self.extract.append(data)
            return f"withdrawal completed. current balance: {self.balance}"

    def view_transactions(self) -> list[dict]:
        return self.extract

def menu():
    print("1- deposit")
    print("2- withdraw")
    print("3- view transactions")
    print("4- log out")
    print("--------------------")

def main():
    account = Account("Natan","0001-00","Nubanks","385 California")

    while True:
        menu()
        option = input("Enter an option: ")
        if option == "1":
            value = float(input("enter a value: "))
            print(account.deposit(value))
        elif option == "2":
            value = float(input("enter a value: "))
            print(account.withdraw(value))
        elif option == "3":
            print(account.view_transactions())
        elif option == "4":
            msg = "goodbye, log out...!"
            print(msg)
            break
        else:
            warning = "try again."
            print(warning)

if __name__ == "__main__":
    main()
