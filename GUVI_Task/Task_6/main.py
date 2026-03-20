#Question 1
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.__balance=balance
        pass
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print('Invalid amount')    

    def withdraw(self,amount): 
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print('Insufficient balance')   
    def getbalance(self):
        return self.__balance         

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest_rate(self):    
         self.interest_rate=self.getbalance()*self.interest_rate/100
         return self.interest_rate

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self,amount):
        self.amount=amount
        if (self.getbalance()-amount)>=self.minimum_balance:
            super().withdraw(amount)
        else:
            return 'Minimunm balance required'
s = SavingsAccount(101, 1000, 5)
s.deposit(500)
s.withdraw(200)
s.calculate_interest_rate()
print("Balance:", s.getbalance()) 

c = CurrentAccount(102, 1000, 500)
c.withdraw(400)   # allowed
c.withdraw(200)   # not allowed (breaks min balance)
print("Balance:", c.getbalance())


#Question2
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary   

    def calculatesalary(self):
        return self.salary


class RegularEmployee(Employee):
    def __init__(self, name, daily_wage, working_days):
        super().__init__(name)
        self.daily_wage=daily_wage
        self.working_days=working_days

    def calculatesalary(self):
        self.salary=self.working_days*self.daily_wage
        return f"Regular Employee Salary: {self.salary}"  
     
class ContractEmployee(Employee):
    def __init__(self,name,daily_wage,working_days):
        super().__init__(name)
        self.daily_wage=daily_wage
        self.working_days=working_days

    def calculatesalary(self):
        self.salary=self.working_days*self.daily_wage
        return f"Contract Employee salary: {self.salary}"
        
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus

    def calculatesalary(self):
        self.salary=self.salary+self.bonus
        return f"manager salary: {self.salary}"  

r=RegularEmployee('Madhu',1000,30)
print(r.calculatesalary())
c=ContractEmployee('Ajay',500,30)
print(c.calculatesalary())
m=Manager('Aari',100000,50000)
print(m.calculatesalary())                      

#Question3
class Vehicle:
    def __init__(self,model,rental_rate):
        self.model=model
        self.rental_rate=rental_rate
        pass
    def calculate_rental(self):
        pass
class Car(Vehicle):
    def __init__(self,model,rental_rate,distance):
        super().__init__(model,rental_rate)
        self.distance=distance
    def calculate_rental(self):
        self.rental=self.rental_rate*self.distance
        return self.rental    
class Bike(Vehicle):
    def __init__(self,model,rental_rate,hours):
        super().__init__(model,rental_rate)
        self.hours=hours
    def calculate_rental(self):
        self.rental=self.rental_rate*self.hours
        return self.rental 
class Truck(Vehicle):
    def __init__(self,model,rental_rate,distance,load_capacity):
        super().__init__(model,rental_rate)
        self.load_capacity=load_capacity
        self.distance=distance
    def calculate_rental(self):
        self.rental=self.rental_rate*self.distance*self.load_capacity
        return self.rental         

c=Car('X',100,35)
print(c.calculate_rental())
b=Bike('Y',150,48)
print(b.calculate_rental())
t=Truck('Z',200,100,50)
print(t.calculate_rental())
