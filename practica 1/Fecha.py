

class Fecha:
    def __init__(self, dd, mm, aa):
        self._dd = dd
        self._mm = mm
        self._aa = aa
    
    
    def getDD(self):
        return self._dd
    def setDD(self, dd):
        self._dd = dd
    
    def getMM(self):
        return self._mm
    def setMM(self, mm):
        self._mm = mm
    
    def getAA(self):
        return self._aa
    def setAA(self, aa):
        self._aa = aa
    
    
    def to_string(self):
        return f"dd: {self._dd}, mm: {self._mm}, aa: {self._aa}"