class BankAccount: 
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def balance_check(self):
    print(self.balance)


egoncalv = BankAccount('Eric', 'Goncalves', 292, 'Corrente', 13, 100.20)  

#egoncalv.deposit(96)
#egoncalv.withdraw(25)
egoncalv.balance_check()

#print(vars(egoncalv))
