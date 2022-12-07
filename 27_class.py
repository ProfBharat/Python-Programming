#creating class and its objects in python  
class fruit:
    
    def __init__(self,name, cost):
        self.name = name
        self.cost = cost

    def greet(self):    #greet() is function
        #print("hai")
        return f"hey, Are you Looking {self.name} its cost is {self.cost}?"
        
fruit1 = fruit("Mango",30)       #mango is an object
fruit2 = fruit("Papaya",50)     #papaya is an object

print(fruit1.greet())

print(fruit2.cost)
#print(mango.name)
#print(f"{papaya.name} its cost is {papaya.cost}")
