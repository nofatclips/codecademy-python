# BitArray code from: http://wiki.python.org/moin/BitArrays
# I've just refactored the methods into a class

# A bit array demo - written for Python 3.0
import array

class BitArray:

    def __init__(self, size, fill=0):
        self.theArray = BitArray.makeBitArray(size,fill)

    @staticmethod
    def makeBitArray(bitSize, fill = 0):
        intSize = bitSize >> 5   # number of 32 bit integers

        # if bitSize != (32 * n) add a record for stragglers
        if (bitSize & 31):                      
            intSize += 1

        if fill == 1: fill = 4294967295 # all bits set
        else: fill = 0 # all bits cleared

        bitArray = array.array('I') # 'I' = unsigned 32-bit integer
        bitArray.extend((fill,) * intSize)
        return(bitArray)

    # testBit() returns 1 if the bit at 'bit_num' is not set to 0.
    def testBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        return(array_name.theArray[record] & mask) != 0

    # setBit() sets 'bit_num' to 1.
    def setBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        array_name.theArray[record] |= mask

    # clearBit() sets 'bit_num' to 0.
    def clearBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = ~(1 << offset)
        array_name.theArray[record] &= mask

    # toggleBit() inverts 'bit_num'
    def toggleBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        array_name.theArray[record] ^= mask

# My Code

class Sieve:

    def __init__(self,maxNum):
        self.maxNum = maxNum
        
        # Array of bits: 0 for non prime, 1 for prime
        # Initialize at all primes except 1
        self._primes = BitArray(maxNum//2+1,1)
        self.setNotPrime(1)

        # The prime number to be used for the next iteration
        # of the sieve. The list of primes is accurate in the
        # range [1,nextIteration**2-1] and if you need to
        # evaluate a bigger number, you must first run more
        # iterations, until the bigger number is in the range
        # Starts at 3 because 2 is treated as a special case
        # and the other even numbers are not even stored
        self.nextIteration = 3

    def setPrime(self,n):
        self._primes.setBit (Sieve._indexFor(n))

    def setNotPrime(self,n):
        self._primes.clearBit (Sieve._indexFor(n))

    def _isMarkedAsPrime(self,n):
        '''True if n is marked with a '1' in the bit array'''
        return self._primes.testBit (Sieve._indexFor(n)) != 0

    @staticmethod
    def _indexFor(n):
        '''Even numbers are not stored, to save space.
           Odd numbers are stored at half of their value'''
        #print ("Index for %i is %i" % (n, n//2))
        return n//2

    def _maxValid(self):
        return self.nextIteration**2-1

    def isPrime(self,n):
        if n>self.maxNum:
            raise IndexError("This sieve accepts values in [1,%i]" % (self.maxNum))
        if n==2: return True
        if not n%2: return False

        # Do as many iterations of the sieve as necessary
        # until we're sure that n is marked as prime if and
        # only if it's actually a prime number
        while n>self._maxValid():
            self._nextIteration()
        return self._isMarkedAsPrime(n)

    def _nextIteration(self):
        #print ("Iteration: %i" % (self.nextIteration) )
        startAt, stopAt, step = \
            self._maxValid()+1, self.maxNum+1, self.nextIteration*2
        for i in range (startAt, stopAt, step):
            #print ("Is not prime: %i" % (i) )
            self.setNotPrime(i)
        self._findNextPrime()

    def _findNextPrime(self):
        self.nextIteration+=2
        while (not self.isPrime(self.nextIteration)):
            self.nextIteration+=1

    @staticmethod
    def checkPrime(n):
        return Sieve(n).isPrime(n)

print (Sieve.checkPrime(1009))
