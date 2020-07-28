class Customer:
    
    num_customers = 1
    max_neg_balance = -50
    
    def __init__(self, last_name, balance):
        self.last_name = last_name
        self.balance = balance     
        self.id = Customer.num_customers
        Customer.num_customers += 1     
        print(self.__str__())
    
    def __str__(self):
        return f"Account # {self.id}: {self.balance:+}€ in balance\n"
            
    def deposit(self, amount):
        self.balance += amount
        print(self.__str__())
        
    def withdraw(self, amount):
        if self.balance - amount < Customer.max_neg_balance:
            print('Withdraw rejected: your current balance is too low')      
        else:
            self.balance -= amount
            
        print(self.__str__())
        

a = Customer('Chen', 20)
a.withdraw(100)
a.deposit(30)
a.withdraw(100)