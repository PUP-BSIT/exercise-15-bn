def citron_kathleen():
    class Person:
        def __init__(self, name, age, birthday):
            self.name = name
            self.age = age
            self.birthday = birthday

        def greet(self): 
            message= "Hello, how are you?"
            print(message)

        def display_name(self):
            print(f"My name is {self.name}")

        def display_age(self):
            print(f"I'm {self.age} years old")

        def display_birthdate(self) :
            print(f"My birthday is {self.birthday}")

        def display_favorites(self):
            print(f"{self.name} loves to play online games") 
            print(f"{self.name} loves to walking in quiet place")
            print(f"{self.name} loves to listening music")

        def display_menu(self):
            while True:
                print("This Menu is All About Me")
                print("(1.) Greetings")
                print("(2.) Name")
                print("(3.) Age")
                print("(4.) Birthday")
                print("(5.) Favorites")
                print("(6.) Return")
                choice = int(input("Enter your choice:")) 

                match choice:
                    case 1:
                       self.greet()
                    case 2:
                       self.display_name()
                    case 3:
                       self.display_age()
                    case 4:
                       self.display_birthdate()
                    case 5:
                       self.display_favorites()
                    case 6:
                        return
                    case _:
                        print("Invalid choice. Please try again.")
                        
    persons = Person(name="Kathleen", age=19, birthday="June 8, 2005")
    persons.display_menu()