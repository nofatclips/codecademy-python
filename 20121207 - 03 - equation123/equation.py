# Find the coefficients (a,b,c) in
#
# y(x) = a * x^2 + b * x + c
#
# knowing y(1), y(2) and y(3).
#
# Let's start with  three valid equations describing the problem:
# 
# y(1) = a + b + c
# y(2) = 4a + 2b + c
# y(3) = 9a + 3b + c
#
# Linear combinations of equations give valid equations, so:
#
# y(3) - 2y(2) = a - b - c <=>
# <=> y(3) - 2y(2) + y(1) = a - b - c + a + b + c = 2a <=>
# <=> a = (y(3) - 2y(2) + y(1)) / 2
#
# And we got the first one! Let's do that again:
#
# y(3) - y(2) = 5a + b <=> b = y(3) - y(2) - 5a
#
# This was an easy one. And the first equation alone is
# enough to get c:
#
# c = y(1) - a - b

def fx(f1, f2, f3):
    a = 0.5 * (f1 + f3) - f2
    b = f3 - f2 - 5*a
    c = f1 - a - b
    #sign1 = "" if b<0 else "+"
    #sign2 = "" if c<0 else "+"
    #return "%g * x**2 %s%g * x %s%g" % (a,sign1,b,sign2,c)
    return "%g * x**2 %+g * x %+g" % (a,b,c)

def test (equation, f1, f2, f3):
    for x,f in [(1,f1),(2,f2),(3,f3)]:
        if not compare (eval(equation), f): return False
    return True

def compare (a,b):
    eps=1e-05
    return abs(a-b)<eps
    
# 033850592228879
f1 = 3.1416
f2 = 2.7183
f3 = 1.6181
equation = fx (f1,f2,f3) # y = -0.3385 * x^2 +0.5922 * x +2.8879
print "y = " + equation
print test (equation,f1,f2,f3)