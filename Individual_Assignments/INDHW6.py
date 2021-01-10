
#8.20
class BankAccount(object):
# self explanatory below , add, substract below
    def __init__(self, bal = 0.0):
        self.accountBal = bal
        
    def withdraw(self, new_amount):
        self.accountBal -= new_amount

    def deposit(self, new_amount):
        self.accountBal += new_amount

    def balance(self):
        return self.accountBal
#test code as written by book
x = BankAccount(700)
print(x.balance())

x.withdraw(70)
print(x.balance())

x.deposit(7)
print(x.balance())






#8.22
#the problem is like the one before, where we estimated pay rates
#we set the person, and payrate as attributes
class Worker(object):
    def __init__(self, name, payrate):
        self.name = name
        self.payrate = payrate
#we create extra pay
    def changeRate(self, extrapayrate):
        self.payrate = extrapayrate
    def pay(self, hours):
        print("Not Implemented")
class HourlyWorker( Worker):
    def pay(self, hours):
        if hours <= 40:
            return self.payrate*hours
        else:
            overtime = hours - 40
            return self.payrate * 40 + self.payrate  * overtime *2
class SalariedWorker(Worker):
#we can use a definite to make 40 permement 
    def pay(self, hours = 40):
        return self.payrate * 40

# test as in the book

w1 = Worker('Joe', 15)
w1.pay(35)

w2 = SalariedWorker('Sue', 14.50)
w2.pay()

w3 = HourlyWorker('Dana', 20)
w3.pay(25)

w3.changeRate(35)
w3.pay(25)



#Assignment 8.34
#for each action, we make a method for that action
class Stat(object):
    def __init__(self):
        self.numbers = []
        
    def add(self, number):
        self.numbers.append(number)
        
    def min(self):
        return min(self.numbers)
    
    def max(self):
        return max(self.numbers)
    
    def sum(self):
        return sum(self.numbers)
    
    def __len__(self):
        return len(self.numbers)
    
    def mean(self):
        return sum(self.numbers)/len(self.numbers)
#if number is there, return true; false otherwise    
    def __contains__(self, number):
        if self.numbers:
            return True
        else:
            return False
        
    def clear(self):
        self.numbers = []

s = Stat()
s.add(2)
s.add(4)
s.add(6)
s.add(8)
print(s.min())
print(s.max())
print(s.sum())
print(len(s))
print(s.mean())
4 in s
s.clear()
    
    #8.35

class Stack(object):
#create methods for each think you want
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)
#pop to remove
    def pop(self):
        return self.stack.pop()
#after pop, it should return False
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
##
###test code 
s = Stack()
s.push('plate 1')
s.push('plate 2')
s.push('plate 3')
print(s)

print(len(s))

print(s.pop())

print(s.pop())

print(s.pop())

print(s.isEmpty())

#8.40
#we use MyError to create our own sense of error, instead of returning or print
class MyError(Exception):
    pass

class BankAccount(object):

    def __init__(self, bal = 0.0):
        self.accountBal = bal
        if self.accountBal < 0:
            raise MyError('Illegal Balance')
        
    def withdraw(self, new_amount):
        if new_amount > self.accountBal:
            raise MyError('Overdraft')
        self.accountBal -= new_amount

    def deposit(self, new_amount):
        if new_amount < 0:
            raise MyError('Negative Deposit')
        self.accountBal += new_amount

    def balance(self):
        return self.accountBal
##    
x = BankAccount(-700)
x.balance()
## please recall x as positive AFTER error

