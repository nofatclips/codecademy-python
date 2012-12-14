class AbstractFiBu(object):
    
    def __init__(self,root,message=""):
        self.root = root
        self.message = message

    def check (self, n):
        return not n%self.root
    
    def write(self, n):
        return self.message

class FizzBuzz(AbstractFiBu):

    def __init__(self):
        super(FizzBuzz,self).__init__(15,"FizzBuzz")

class Fizz(AbstractFiBu):

    def __init__(self):
        super(Fizz,self).__init__(3,"Fizz")

class Buzz(AbstractFiBu):

    def __init__(self):
        super(Buzz,self).__init__(5,"Buzz")
    
class Nope:

    @staticmethod
    def check (n):
        return True
    
    @staticmethod
    def write(n):
        return n

class Game:
    
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        criteria = [FizzBuzz(), Fizz(), Buzz(), Nope]
        lastNum=self.n+1
        for num in range (1,lastNum):
            for criterion in criteria:
                if criterion.check(num):
                    yield criterion.write(num)
                    break

for turn in Game(50): print turn