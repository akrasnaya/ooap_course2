class General():
    def __init__(self):
        pass
    
    def void(self):
        pass

class Any(General):
    pass

class None(General, Any):
    def __init__(self):
        super(None, self).__init__()
    
    def void(self):
        super(None, self).void()
