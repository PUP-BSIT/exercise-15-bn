import os

def quiambao_mapatricia():
    class Cat:
        def __init__(self, name, age, birthday):
            self.name = name
            self.age = age
            self.birthday = birthday

        def greet(self): 
            message = "Hi, There! Welcome to My Menu"
            print(message)
            input("Please press enter to continue")
           
        def display_name(self):
            print(f"The name of my cat is {self.name}")
            input("Please press enter to continue")

        def display_age(self):
            print(f"{self.name} is {self.age} weeks old")
            input("Please press enter to continue")
            
        def display_favorite_birthdate(self) :
            print(f"{self.name}'s birthday is on {self.birthday} ")
            input("Please press enter to continue")

        def display_about_pochi(self):
            print(f"{self.name} loves to sleep\n")
            print(f"{self.name} loves to play\n")
            print(f"{self.name} loves to eat\n")
            print(f"{self.name} is a tri-color cat\n")
            print(f"{self.name} have a light gray eyes\n")
            print(f"{self.name} is a female cat\n")
            input("Please press enter to continue")
        
        def menu(self):
           while True:
                print("This Menu is All About Pochi")
                print("[1.] Greetings")
                print("[2.] Name")
                print("[3.] Age")
                print("[4.] Birthday")
                print("[5.] About Pochi")
                print("[6.] Return")
                choice = int(input("Enter your choice:")) 

                match choice:
                    case 1:
                       self.greet()
                    case 2:
                       self.display_name()
                    case 3:
                       self.display_age()
                    case 4:
                       self.display_favorite_birthdate()
                    case 5:
                       self.display_about_pochi()
                    case 6:
                       return
                    case _:
                     print("Invalid choice.")
                     input("Please press enter to continue")  
                os.system('cls')
                        
    Cat = Cat(name="Pochi", age=6, birthday="November 22, 2024")
    Cat.menu() 