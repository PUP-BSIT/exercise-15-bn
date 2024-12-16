class Cat:
        def __init__(self, name, breed, food):
            self.name = name
            self.breed = breed
            self.food = food
            self.energy = 100  # Add an energy attribute

        def greet(self):
            print(f"Meow. Hi! I'm {self.name}, a {self.breed} cat.")

        def feed(self):
            print(f"{self.name} is hungry and wants to eat some {self.food}!")
            
        def play(self):
            if self.energy >= 30:
                print(f"{self.name} is ready to play! Let's chase some yarn!")
                self.energy -= 20  # Decrease energy after playing
            else:
                print(f"{self.name} is a bit tired. Maybe some"
                       " petting is in order?")

        def pet(self):
            self.energy += 30  # Increase energy after being petted

            if self.energy > 100:
                 self.energy = 100
                 
            print(f"{self.name} purrs contentedly after being petted."
                  " Energy level increased")
        
        def mood(self):
            print(f"\n{self.name}'s energy level is {self.energy}!")    
            if self.energy <= 20:
                print(f"\n{self.name} is curled up in a sunny spot,"
                      " taking a nap. Zzz..")
                self.energy = 100  # Reset energy after napping
            else:
                print(f"{self.name} is stretching and looking playful."
                      " Perhaps some playtime?")

def relente_patricia():
            cat_name = input("What's your cat's name? ")
            cat_breed = input("What breed is your cat? ")
            cat_food = input("What's your cat's favorite food? ")

            obj = Cat(cat_name, cat_breed, cat_food)

            def menu():
                while True:
                    print(f"\nWhat would you like to do with {cat_name}?")
                    print("1. Greet")
                    print("2. Feed")
                    print("3. Play")
                    print("4. Pet")
                    print("5. Check the mood")       
                    print("6. Back")

                    choice = int(input("Enter your choice: "))

                    match choice:
                        case 1:
                            obj.greet()
                        case 2:
                            obj.feed()
                        case 3:
                            obj.play()
                        case 4:
                            obj.pet()
                        case 5:
                            obj.mood()  
                        case 6:
                            print(f"Bye! See you and {cat_name} again soon.")
                            return
                        case _:
                            print("Invalid choice. Please try again.")

            menu()
relente_patricia()

