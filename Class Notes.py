# Defining a class
class Cat(object):
    def __init__(self, color, pattern):  # TWO Underscores before and after
        # Things that a Cat has
        self.color = color
        self.pattern = pattern
        self.state = "happy"
        self.hungry = False

    # Things that a Cat can do
    def jump(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state t the cats
print(cute_cat.color)
print(cute_cat2.state)
print(cute_cat2.color)

= "happy"
        print("You play with the cat")


# Instantiating (creating) two cats
cute_cat = Cat("brown", "Spots")
cute_cat2 = Cat("gray", "no spots")


# Getting information abou
cute_cat.jump()
print(cute_cat.state)
print(cute_cat2.state)

cute_cat.play()
print(cute_cat.state)


class Car(object):
    def __init__(self, color, brand, stripe):
        self.color = color
        self.brand = brand
        self.stripe = stripe
        self.engineOn = False

    def turn_on(self):
        if self.engineOn:
            print("Nothing Happens")
        else:
            print("The engine turns on")
            self.engineOn = True

    def move_forward(self):
        if self.engineOn:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.engineOn:
            self.engineOn = False
            print("The Engine is off")
        else:
            print("Nothing happens")


my_car = Car(4, "Subaru", "Blue")

my_car.turn_on()
my_car.move_forward()
my_car.turn_off()

