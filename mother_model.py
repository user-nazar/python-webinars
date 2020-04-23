from abc import ABC, abstractmethod


@abstractmethod
class AbstractParent(ABC):
    def hello_friend(self):
        raise NotImplementedError


class Mother:
    def __init__(self, age=0):
        self.age = age
        print("mother constructor")

    def do_work(self):
        print("I'm working")

    def playing(self):
        print("I play football")

    def do_house_work(self):
        print("listen music")


class Father(AbstractParent):
    def __init__(self):
        print("father constructor")

    def play_guitar(self):
        print("father is playing guitar")

    def do_house_work(self):
        print("sit in the sofa and drink")


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Father.__init__(self)
        Mother.__init__(self, age=age)

    def do_work(self):
        print("I'm working like a horse")

    def hello_friend(self):
        pass


class Friend:
    pass


def greet_mother(mother: Mother):
    print("hello mother!!!")
    mother.do_work()


def greet_father(father: Father):
    print("time for beer")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    # mother.do_work()

# change object class
# daughter.__class__== Friend
greet_mother(daughter)
greet_father(daughter)
daughter.hello_friend()
daughter.do_house_work()
daughter.playing()

for x in [daughter]:
    x.do_house_work()

# list
povtorka_list = ["matan_2", "programming_2", "superprise"]

# tuple
vasian = ("11 years", 2, 3.14, daughter)

# set
my_set = {23, 11, 10, 10, "call"}
print(my_set)

# frozen set
another_set = frozenset(["di", "mi", "do"])

# dictionary
my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple as a key"}
