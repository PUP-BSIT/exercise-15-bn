class Cat:
    def __init__(self, name, breed, food):
        self.name = name
        self.breed = breed
        self.food = food
        self.energy = 100  # Add an energy attribute

    def choice_1(self):
        print(f"Meow. Hi! I'm {self.name}, a {self.breed} cat.")

    def choice_2(self):
        print(f"{self.name} is hungry and wants to eat some {self.food}!")
           
    def choice_3(self):
        if self.energy >= 40:
            print(f"{self.name} is ready to play! Let's chase some yarn!")
            self.energy -= 20  # Decrease energy after playing
        else:
            print(f"{self.name} is a bit tired. Maybe some petting is in order?")

    def choice_4(self):
        self.energy += 30  # Increase energy after being petted
        print(f"{self.name} purrs contentedly after being petted. Energy level increased!")
    
    def choice_5(self):
        print(f"\n{self.name}'s energy level is {self.energy}!")    
        if self.energy <= 20:
            print(f"\n{self.name} is curled up in a sunny spot, taking a nap. Zzz...")
            self.energy = 100  # Reset energy after napping
        else:
            print(f"{self.name} is stretching and looking playful. Perhaps some playtime?")

def relente_patricia():
    cat_name = input("What's your cat's name? ")
    cat_breed = input("What breed is your cat? ")
    cat_food = input("What's your cat's favorite food? ")

    obj = Cat(cat_name, cat_breed, cat_food)

    while True:
        print(f"\nWhat would you like to do with {cat_name}?")
        print("1. Talk to the cat")
        print("2. Feed")
        print("3. Play")
        print("4. Pet")
        print("5. Check the mood")       
        print("6. Back")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                obj.choice_1()
            case 2:
                obj.choice_2()
            case 3:
                obj.choice_3()
            case 4:
                obj.choice_4()
            case 5:
                obj.choice_5()       
            case 6:
                print(f"Bye! See you and {cat_name} again soon.")
                return
            case _:
                print("Invalid choice. Please try again.")

relente_patricia()

