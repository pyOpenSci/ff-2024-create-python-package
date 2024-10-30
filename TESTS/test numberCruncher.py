"""TEST to check module numberCruncher"""
from supernormal.numberCruncher import crunch
def testCrucher():
    """test output of the crunch"""
    assert crunch(1,2) == 3
