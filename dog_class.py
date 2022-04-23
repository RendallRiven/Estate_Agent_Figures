class Dog:

# class variable shared by all instances
    species = ["canis lupus"]
    def __init__(self, name, color):
        self.name = name
        self.state = "sleeping"
        self.color = color

    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "sit":
            self.state = "sit"
            print(self.name,"is sitting")
        else:
            self.state = "wag tail"

    def bark(self, freq):
        for i in range(freq):
            print("[" + self.name
                + "]: Woof!")

bello = Dog("bello", "black")
alice = Dog("Alice", "white")

print(bello.color)
alice.command("sit")
alice.command("alice")
print(Dog)