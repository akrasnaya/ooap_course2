class General():

    def __init__(self):
        pass

    def copy(self):
        copy = self
        return copy
    
    def clone(self):
        clone = self.deepcopy
        return clone
    
    def compare(self, obj2):
        pass
    
    def print(self):
        print(self)
        
    def string_format(self):
        return str(self)
    
    def check_type(self):
        return self.isinstance()
    

class Any(General):
    
    def __init__(self):
        super(Any, self).__init__()
