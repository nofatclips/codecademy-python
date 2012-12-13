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

def play (n):
    criteria = [FizzBuzz(), Fizz(), Buzz(), Nope]
    for num in range (1,n+1):
        for criterion in criteria:
            if criterion.check(num):
                print criterion.write(num)
                break

play(20)