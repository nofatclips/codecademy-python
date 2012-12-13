from random import choice

class RootBeer(object):
    
    def __init__(self, n):
        self.bottles = n
    
    def parameters(self):
        return {"num": self.bottles, "drink": Song.drink}
    
    def nextVerse(self):
        return Song.verse(self.bottles-1)
    
    def onTheWall(self):
        return "%(num)i bottles of %(drink)s on the wall" % \
            self.parameters()
    
    def bottlesOfBeer(self):
        return "%(num)i bottles of %(drink)s" % \
            self.parameters()
    
    def oneLess(self):
        return "Take one down, pass it around"
            
    def firstLine(self):
        print "%s, %s." % (self.onTheWall(), self.bottlesOfBeer())
        return self
    
    def secondLine(self):
        next = self.nextVerse()
        print "%s, %s." % (self.oneLess(), next.onTheWall())
        return next

class RootBeerAlt(RootBeer):

    def __init__(self,n):
        super(RootBeerAlt, self).__init__(n)

    def oneLess(self):
        return "If one of those bottles should happen to fall"
        
class OneBeer(RootBeer):

    def __init__(self):
        super(OneBeer, self).__init__(1)

    def onTheWall(self):
        return "One bottle of %(drink)s on the wall" % \
            self.parameters()
    
    def bottlesOfBeer(self):
        return "One bottle of %(drink)s" % \
            self.parameters()

class OneBeerAlt(OneBeer):

    def __init__(self):
        super(OneBeerAlt, self).__init__()

    def secondLine(self):
        print "If that one bottle should happen to fall,",
        print "what a waste of alcohol!"
        return None

class NoBeers(RootBeer):
    def __init__(self):
        super(NoBeers, self).__init__(0)

    def nextVerse(self):
        return Song.firstVerse()

    def onTheWall(self):
        return "No more bottles of %(drink)s on the wall" % \
            self.parameters()
    
    def oneLess(self):
        return "Go to the store and buy some more"

    def bottlesOfBeer(self):
        return "No more bottles of %(drink)s" % \
            self.parameters()

class Song:

    maxBottles = 99
    drink = "rootbeer"
    
    @staticmethod
    def verse(n):
        alt = choice([True, False])
        if n==1:
            return OneBeerAlt() if alt else OneBeer()
        if n==0: 
            return NoBeers()
        return RootBeerAlt(n) if alt else RootBeer(n)
    
    @staticmethod
    def firstVerse():
        return Song.verse(Song.maxBottles)

nextVerse = Song.firstVerse()
while (nextVerse):
    nextVerse = nextVerse.firstLine().secondLine()