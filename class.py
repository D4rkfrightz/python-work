# class Animal:
#     def __init__(self):
#         self.name = "saad"

# myAnimal = Animal()
# print(myAnimal.name)


class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 10
    
    def calculate_age(self):
        print("name of animal is", self.name, "age is", self.age)


# myAnimal2 = Animal("daas")
# print(myAnimal2.name)
