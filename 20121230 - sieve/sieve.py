# BitArray code from: http://wiki.python.org/moin/BitArrays
# I've just refactored the methods into a class

# A bit array demo - written for Python 3.0
import array

class BitArray:

    def __init__(self, size, fill=0):
        self.theArray = BitArray.makeBitArray(size,fill)

    @staticmethod
    def makeBitArray(bitSize, fill = 0):
        intSize = bitSize >> 5                   # number of 32 bit integers
        if (bitSize & 31):                      # if bitSize != (32 * n) add
            intSize += 1                        #    a record for stragglers
        if fill == 1:
            fill = 4294967295                                 # all bits set
        else:
            fill = 0                                      # all bits cleared

        bitArray = array.array('I')          # 'I' = unsigned 32-bit integer
        bitArray.extend((fill,) * intSize)
        return(bitArray)

    # testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
    def testBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        return(array_name.theArray[record] & mask)

    # setBit() returns an integer with the bit at 'bit_num' set to 1.
    def setBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        array_name.theArray[record] |= mask
        return(array_name.theArray[record])

    # clearBit() returns an integer with the bit at 'bit_num' cleared.
    def clearBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = ~(1 << offset)
        array_name.theArray[record] &= mask
        return(array_name.theArray[record])

    # toggleBit() returns an integer with the bit at 'bit_num' inverted, 0 -> 1 and 1 -> 0.
    def toggleBit(array_name, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        array_name.theArray[record] ^= mask
        return(array_name[record])

# My Code

class Sieve:

    def __init__(self,maxNum):
        self.maxNum = maxNum
        
        # Array of bits: 0 for non prime, 1 for prime
        self._primes = BitArray(maxNum+1,1)
        self.setNotPrime(0)
        self.setNotPrime(1)

        # The prime number to be used for the next iteration
        # of the sieve. The list of primes is accurate in the
        # range [1,nextIteration**2-1] and if you need to
        # evaluate a bigger number, you must first run more
        # iterations, until the bigger number is in the range
        self.nextIteration = 2

    def setPrime(self,n):
        self._primes.setBit (n)

    def setNotPrime(self,n):
        self._primes.clearBit (n)

    def _isMarkedAsPrime(self,n):
        return self._primes.testBit (n) != 0

    def _maxValid(self):
        return self.nextIteration**2-1

    def isPrime(self,n):
        while n>self._maxValid():
            self._nextIteration()
        if n>self.maxNum: raise IndexError("This sieve accepts values in [1,%i]" % (self.maxNum))
        return self._isMarkedAsPrime(n)

    def _nextIteration(self):
        #print ("Iteration: %i" % (self.nextIteration) )
        startAt = self._maxValid()+1
        for i in range (startAt, self.maxNum+1, self.nextIteration):
            #print ("Is not prime: %i" % (i) )
            self.setNotPrime(i)
        self._findNextPrime()

    def _findNextPrime(self):
        self.nextIteration+=1
        while (not self._isMarkedAsPrime(self.nextIteration)):
            self.nextIteration+=1

sieve = Sieve(100)
for i in range(100):
    if sieve.isPrime(i):
        print(i)
