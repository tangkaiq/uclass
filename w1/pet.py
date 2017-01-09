class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    #print
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)



class Dog(Pet):

    def __init__(self, name):
        Pet.__init__(self, name, "Dog")

class Cat(Pet):
    def __init__(self,name,color):
        Pet.__init__(self, name, "Cat")
        self.color = color;

    def __str__(self):
        return "%s is a %s which its color is %s" % (self.name, self.species,self.color)
    
