
class fruit:
    
    def __init__(self,name, cost):
        self.name = name
        self.cost = cost

    def greet(self):
        #print("hai")
        return f"hey Are you Looking {self.name}?"
mango = fruit("Mango",30)
papaya = fruit("Papaya",50)

print(mango.greet())
print(mango.cost)
print(mango.name)
print(f"{papaya.name} its cost is {papaya.cost}")