from collections import deque

class DisassemblyLine:

    def __init__ (self):
        self._set = set()
        self._queue = deque()

    def push (self, value):
        #print ("Pushing " + value)
        self._set.add(value)
        self._queue.append(value)

    def pop (self):
        #print ("Popping")
        return self._queue.popleft()

    def __bool__ (self):
        #print ("Checking non zero")
        return True if self._queue else False

    def __len__ (self):
        #print ("Len")
        return len(self._set)

    def __call__ (self):
        return self._set

class SubstringGenerator:

    def __init__(self, word):
        self.word = word
        self._subList = self.count()
        #self.count()

    def count(self):
        #theList, strings = set(), deque()
        counter = DisassemblyLine()
        #theList.add(self.word)
        #strings.append(self.word)
        counter.push(self.word)

        l=0
        #while strings:
        while counter:
            #string = strings.popleft()
            string = counter.pop()
            l, previousL = len(string),l
            lWord, rWord = string[:-1], string[1:]
            if l!=previousL and lWord:
                #theList.add(lWord)
                #strings.append(lWord)
                counter.push(lWord)
            if rWord:
                #theList.add(rWord)
                #strings.append(rWord)
                counter.push(rWord)

        return counter()

    # Delegate protocols to the subList object

    def __str__(self): # Invoked when you call str()
        return str(self._subList)

    def __len__ (self): # Invoked when you call len()
        return len(self._subList)

    def __iter__ (self): # Invoked on enumeration
        return iter(self._subList)

subs = SubstringGenerator("abbaz")
print (*subs, sep='\n') #Enumerate subs
print ("Count: %i" % len(subs))

