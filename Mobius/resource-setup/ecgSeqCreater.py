import random
import time

class EcgSeqCreater():
    def __init__(self, ecgMin, ecgMax, changeMax, strangeRate):
        self.setValues(ecgMin, ecgMax, changeMax, strangeRate)

    def setValues(self, ecgMin, ecgMax, changeMax, strangeRate):
        self.ECG_MAX = ecgMax
        self.ECG_MIN = ecgMin
        self.CHANGE_MAX = changeMax
        self.STRANGE_RATE = strangeRate
        self.prevEcg = self.randECG() 
    
    def randECG(self):
        return random.random() * (self.ECG_MAX - self.ECG_MIN) + self.ECG_MIN

    def randNormalECG(self):
        self.prevEcg += (random.random() - 0.5) * self.CHANGE_MAX
        if(self.prevEcg > self.ECG_MAX):
            self.prevEcg = self.ECG_MAX
        if(self.prevEcg < self.ECG_MIN):
            self.prevEcg = self.ECG_MIN
        return self.prevEcg

    def randAbnormalECG(self):
        self.prevEcg = self.randNormalECG()
        if(random.random() < self.STRANGE_RATE):
            return self.randECG()
        return self.prevEcg