from math import sin, pi, radians, degrees, sqrt, acos
from inspect import stack

class Triangle:

    # Private initializer. Do not call directly. Use given*() methods
    def __init__(self, a, b, c, alpha=None, beta=None, gamma=None, name=None):
        if not getattr(self, stack()[1][3], None):
            raise SystemError("Just for today, Python is Java...")
        self.a, self.b, self.c = a, b, c
        self.alpha, self.beta, self.gamma = alpha, beta, gamma
        self.name = name

    def angles (self):
        return self.alpha, self.beta, self.gamma

    def sides (self):
        return self.a, self.b, self.c

    def perimeter (self):
        return self.a + self.b + self.c

    # Heron's formula
    def area (self):
        s = self.perimeter()/2.0
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def isEquilateral (self):
        return self.a == self.b and self.b == self.c

    def isIsosceles (self):
        return not self.isEquilateral() and \
               (self.a == self.b or self.b == self.c or self.a == self.c)

    def isScalene (self):
        return not (self.isEquilateral() or self.isIsosceles())

    def isRight (self):
        return 89.9<max(self.angles())<90.1

    def isObtuse (self):
        return not self.isRight() and max(self.angles())>90

    def isAcute (self):
        return not (self.isRight() or self.isObtuse())

    def __lt__ (self, that):
        return self.area() < that.area()

    def __eq__ (self, that):
        return self.area() == that.area()

    def __height__ (self, base):
        return self.area()*2/base

    def heightBaseA (self):
        return self.__height__(self.a)

    def heightBaseB (self):
        return self.__height__(self.b)

    def heightBaseC (self):
        return self.__height__(self.c)

    # Non instance methods

    def checkAngles (self):
        _180 = self.alpha + self.beta + self.gamma
        return 179.9<_180<180.1

    def checkAnglesAndSides (self):
        r1 = self.a / sin(radians(self.alpha))
        r2 = self.b / sin(radians(self.beta))
        r3 = self.c / sin(radians(self.gamma))
        normalize = max(self.a, self.b, self.c)
        check = sqrt ( (r1-r2)**2 + (r2-r3)**2 + (r1-r3)**2 ) / normalize
        return check<=0.1

    def checkSides (self):
        return (self.a + self.b >= self.c) and \
               (self.a + self.c >= self.b) and \
               (self.b + self.c >= self.a)

    def _addAngles (self):
        self.alpha, self.beta, self.gamma = self.findAngles()
        return self

    cosineLaw = lambda a,b,c:degrees(acos((b*b+c*c-a*a)/(2.0*b*c)))

    def findAngles (self):
        return Triangle.cosineLaw (self.a, self.b, self.c), \
               Triangle.cosineLaw (self.b, self.c, self.a), \
               Triangle.cosineLaw (self.c, self.a, self.b)

    def triangleSideType (self):
        return "equilateral" if self.isEquilateral() else \
               "isosceles" if self.isIsosceles() else \
               "scalene"

    def triangleAngleType (self):
        return "right" if self.isRight() else \
               "acute" if self.isAcute() else \
               "obtuse"

    def __str__ (self):
        ret  = "Properties for triangle %s:\n" % \
               self.name if self.name else "with no name"
        ret += "Sides: a = %g, b = %g, c = %g\n" % self.sides()
        ret += "Angles: alpha = %g°, beta = %g°, gamma = %g°\n" % self.angles()
        ret += "Area: %g - Perimeter: %g\n" % (self.area(), self.perimeter())
        ret += "Type: %s and %s\n" % \
               (self.triangleSideType(), self.triangleAngleType())
        ret += "Heights: %g (for a), %g (for b), %g (for c)\n" % \
               (self.heightBaseA(), self.heightBaseB(), self.heightBaseC())
        return ret

    # Builder methods. Use these instead of the constructor

    @staticmethod
    def givenSides (a, b, c, name=None):
        t = Triangle(a,b,c, name=name)
        if not t.checkSides():
            raise ValueError ("Triangle Inequality not satisfied by given sides.");
        return t._addAngles()

    @staticmethod
    def givenSidesAndAngles (a, b, c, alpha, beta, gamma, name=None):
        '''a, b and c are the sides of the triangle
        alpha is the angle opposite to a, beta opposite to b, gamma to c'''
        t = Triangle(a,b,c,alpha,beta,gamma,name)
        if not t.checkAngles():
            raise ValueError ("Internal angles does not sum up to 180 degrees.")    
        if not t.checkAnglesAndSides():
            raise ValueError ("Sine law not satisfied by given sides and angles.")
        return t
        

approx = Triangle.givenSidesAndAngles(45,12,54,40,10,130,"Approx")
precise = Triangle.givenSides(45,12,54, name="Precise")
right = Triangle.givenSides(3,4,5, name="Right")
print (approx, precise, right, sep="\n")

bigger = max (approx, precise, right)
print ("And the bigger is: %s" % bigger.name)
