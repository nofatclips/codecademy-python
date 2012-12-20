from random import choice

class Verse(object):
    
    def __init__(self, song, n):
        self.song = song
        self.bottles = n
    	self._next = None
    
    def parameters(self):
        return {
			"num": self.bottles, 
			"drink": self.song.drink,
			"type": self.song.drink.type
		}
    
    def nextVerse(self):
        if self._next: return self._next
        self._next = self.song.verse(self.bottles-1)
        return self._next
    
    def onTheWall(self):
        return "%(num)i bottles of %(drink)s on the wall" % \
            self.parameters()
    
    def bottlesOfBeer(self):
        return "%(num)i bottles of %(drink)s" % \
            self.parameters()
    
    def oneLess(self):
        return "Take one down, pass it around"
            
    def firstLine(self):
        return "%s, %s." % (self.onTheWall(), self.bottlesOfBeer())
        #return self
    
    def secondLine(self):
        next = self.nextVerse()
        return "%s, %s." % (self.oneLess(), next.onTheWall())
        #return next
	
    def __str__(self):
        return "%s\n%s" % (self.firstLine(), self.secondLine())		

class AltVerse(Verse):

    def __init__(self, song, n):
        super(AltVerse, self).__init__(song, n)

    def oneLess(self):
        return "If one of those bottles should happen to fall"
        
class OneBeerVerse(Verse):

    def __init__(self, song):
        super(OneBeerVerse, self).__init__(song, 1)

    def onTheWall(self):
        return "One bottle of %(drink)s on the wall" % \
            self.parameters()
    
    def bottlesOfBeer(self):
        return "One bottle of %(drink)s" % \
            self.parameters()

class OneBeerAltVerse(OneBeerVerse):

    def __init__(self, song):
        super(OneBeerAltVerse, self).__init__(song)

    def secondLine(self):
        return "If that one bottle should happen to fall, " \
			+ "what a waste of %(type)s!" % self.parameters()
	
    def nextVerse(self):
        return None

class NoBeersVerse(Verse):
    def __init__(self, song):
        super(NoBeersVerse, self).__init__(song, 0)

    def nextVerse(self):
        if self._next: return self._next
        self._next = self.song.firstVerse()
        return self._next

    def onTheWall(self):
        return "No more bottles of %(drink)s on the wall" % \
            self.parameters()
    
    def oneLess(self):
        return "Go to the store and buy some more"

    def bottlesOfBeer(self):
        return "No more bottles of %(drink)s" % \
            self.parameters()

class Drink(object):
	
	def __init__(self, name, type=None):
		self.name=name
		self.type=type if type else name

	def __str__(self):
		return self.name

class RootBeer(Drink):

	def __init__(self):
		super(RootBeer, self).__init__("rootbeer", "alcohol")

class Milk(Drink):

	def __init__(self):
		super(Milk, self).__init__("milk")
		
class Song(object):

    def __init__(self, maxBottles = 99, drink="rootbeer"):
        self.maxBottles = maxBottles
        self.drink = drink
        self.currentVerse = None
    
    def __iter__(self):
        self.currentVerse = self.firstVerse()
        while (self.currentVerse):
            yield self.currentVerse
            self.currentVerse = self.currentVerse.nextVerse()

    def verse(self, n):
        alt = choice([True, False])
        if n==1:
            return OneBeerAltVerse(self) if alt else OneBeerVerse(self)
        if n==0: 
            return NoBeersVerse(self)
        return AltVerse(self, n) if alt else Verse(self, n)
    
    def firstVerse(self):
        return self.verse(self.maxBottles)
    
    def sing(self):
        for verse in self:
            print verse

Song(99,RootBeer()).sing()