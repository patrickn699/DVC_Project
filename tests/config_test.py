import pytest

class OutOfRange(Exception):
    def __init__(self,message = 'the value is out of range'):

        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises(OutOfRange):
        if a not in range(10,20):
            raise OutOfRange

   
    
    #assert a== b