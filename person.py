class People:
    position=1
    shape=''
    '''def __init__(self):
        self.position=1
        #self.shape'''
class Person(People):
    def __init__(self):
        #By default the mario is on the ground
        self.shape='m' #m=>Short Person and M=>Large Person
        self.position=1
        self.height=0   
player=Person()

class Enemy:
    def __init__(self,start=68,end=0,osc=False):
        self.startPosition=start
        self.endPosition=end
        self.position=start
        self.oscillate=osc
        self.currDirection="RL"