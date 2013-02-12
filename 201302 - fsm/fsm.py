# FSM.py

numbers = [1,2,9,8,6]

def ImmediatelyInvoke(function):
    return function()

class Transition(object):
    
    def __init__(self, trigger, destination):
        self.trigger = trigger
        self.to = destination
        
class State(object):
    
    def __init__(self, name, transitions, output=False):
        self.name = name
        self.transitions = transitions
        self.output = output

class FSM(object):
    
    def __init__(self, sequence=None):
        self.states = {}
        self._state = None
        self.sequence = sequence
        self.start = None

    def addState(self, state, start=False):
        self.states[state.name] = state
        if start: self.setStart(state.name)

    def setStart(self, start):
        self._state = start
        self.start = start

    def addStates(self, *states):
        for state in states:
            self.addState(state)
    
    def addStartState(self, state):
        self.addState(state, True)

    def getSymbols(self):
        for symbol in self.sequence:
            yield symbol

    def startState(self):
        return self.start

    def reset(self):
        self._state = self.startState()
        
    def getTransitions(self):
        return self.states[self._state].transitions

    def step(self, symbol):
        transitions = self.getTransitions()
        for transition in transitions:
            if (transition.trigger(symbol)):
                self._state = transition.to
                return

    def output(self):
        return self.states[self._state].output

@ImmediatelyInvoke
def array_front9():

    def buildMachine():
        
        # Machine definition

        #Triggers

        # Generic Trigger for character not matching
        not9 = lambda x:x!=9

        # All Catching trigger
        alwaysTrue = lambda x=None:True

        # States

        # Successful transition
        found9 = Transition (lambda x:x==9, "found9")

        # Transition Sets

        # Start state: ready to receive the first character
        firstChar = State ("firstChar", [
            found9,
            Transition(not9, "secondChar")
        ])

        # State 2: Received one character and it wasn't a 9
        secondChar = State ("secondChar", [
            found9,
            Transition(not9, "thirdChar")
        ])

        # State 3: Received two characters and none was a 9
        thirdChar = State ("thirdChar", [
            found9,
            Transition(not9, "fourthChar")
        ])

        # State 4: Received three characters and none was a 9
        fourthChar = State ("fourthChar", [
            found9,
            Transition(not9, "sink")
        ])

        # Sink state: lasciate ogni speranza, voi ch'entrate
        sink = State ("sink", [Transition(alwaysTrue, "sink")], False)

        # Success state: found 9
        found9 = State ("found9", [Transition(alwaysTrue, "found9")], True)

        # FSM

        fsm = FSM()
        fsm.addStartState(firstChar)
        fsm.addStates(secondChar, thirdChar, fourthChar, sink, found9)

        return fsm

    fsm = buildMachine()

    def closure(numbers):
        fsm.reset()
        for n in numbers:
            fsm.step(n)
        return fsm.output()

    return closure

print (array_front9(numbers))
