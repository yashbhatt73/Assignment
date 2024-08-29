#Q1. The Person class has a constructor that takes name and age as arguments and assigns them to the object's attributes. 
# The introduce method is then invoked on the object to introduce the person.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f'My name is {self.name} and I am {self.age} years old.')
p=person('Yash', 26)
p.introduce()


#Q2.The Car class has a constructor that takes brand and model as arguments and assigns them to the object's attributes. 
#The display_info method is then invoked on the object to display the car's brand and model.

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f'Brand of car is {self.brand} and model is {self.model}')
c=car('Ford','Classic Mustang')
c.display()


#Q3.the BankAccount class has a constructor that takes account_number and balance as arguments and assigns them to the object's attributes. 
#The display_balance method is then invoked on the object to display the account number and balance

class bank:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def display(self):
        print(f'Hello your account number is {self.account_number} and balance is {self.balance}')
a=bank('100',10000)
a.display()


#Q4.The MobilePhone class has a constructor that takes brand and model as arguments and assigns them to the object's attributes. 
#The make_call method is then invoked on the object to make a call with the phone.

class mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def make_call(self,number):
        self.number=number
        print(f'You are reciving call with {self.number} this number and the phone is {self.model} of {self.brand} brand')
p=mobile('Asus','ROG 7')
p.make_call('9009849006')


# Q5.The Book class has a constructor that takes title and author as arguments and assigns them to the object's attributes. 
# The display_info method is then invoked on the object to display the book's title and author

class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f'The title of the book is {self.title} and author is {self.author}')
b=book('The Naga Warriors','Akshat Gupta')
b.display()



# Q6.Vehicles: Create a base class called Vehicle with attributes such as make, model, and year. Implement two subclasses Car and Motorcycle that 
# inherit from Vehicle.Add additional methods to the subclasses, such as start_engine() and stop_engine(), and handle any specific behavior or rules 
# for each vehicle type.

class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f'The year of making vehicle is {self.year} made by {self.make} company and model is {self.model}')
    def start(self):
        print('Engine started')
    def stop(self):
        print('Engine stopped')
        
class car(vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def start(self):
        print(f'The cars engine has started')
    def stop(self):
        print(f'The cars engine has stoped')
        
class motorcycle(vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def start(self):
        print(f'The motorcycles engine has started')
    def stop(self):
        print(f'The motorcycles engine has stoped')
   
c=car('Ford','Mustang Cobra',2015)
m=motorcycle('Kawasaki','Ninja zx10R',2023)
c.display()  
c.start()
c.stop()

m.display()   
m.start()            
m.stop()           



# Q7.Animals: Create a base class called Animal with methods such as eat() and sleep(). Implement two subclasses Dog and Cat that inherit from Animal. 
# Add additional methods to the subclasses, such as bark() for dogs and meow() for cats, and handle any specific behavior or rules for each animal type.

class animal:
    def eat(self):
        print('Animal wants something for eat')
    def sleep(self):
        print('Animal wants to sleep')

class dog(animal):
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f'{self.name} is barking Woof Woof')
    def sleep(self):
        print(f'{self.name} is sleeping on the sofa')

class cat(animal):
    def __init__(self,name):
        self.name=name
    def meow(self):
        print(f'{self.name} is meowing Meow')
    def sleep(self):
        print(f'{self.name} sleeping on bed')

d=dog('Tommy')
c=cat('Mani')
d.eat() 
d.sleep() 
d.bark() 
c.eat()                          
c.sleep()                              
c.meow()                        
   