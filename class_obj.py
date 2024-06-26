class Person:
    def __init__ (self , name , age):
         
         self.name = name
         self.age = age

    def person_info(self):
     
          return f"{self.name} is {self.age} years old"

alice = Person("Alice", 25)
bob = Person("Bob" , 30)

print(alice. person_info())
print(bob. person_info())
