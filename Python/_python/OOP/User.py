class User:
    def __init__(self,name,email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposite(self,amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("User:" ,self.name, ", Balance:" , self.account_balance)
    def transfer_money(self, name, amount):
        self.make_withdrawl(amount)
        #self.account_balance -= amount
        name.make_deposite(amount)
        #name.account_balance += amount
        return name.account_balance

veer = User("Veer", "veer@python.com")
veeru = User("Veeru", "veeru@python.com")

veer.make_deposite(500)
veeru.make_deposite(300)
veeru.transfer_money(veer, 300)
veer.display_user_balance()
veeru.display_user_balance()