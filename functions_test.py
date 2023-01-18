import unittest
from functions import *

def test_generator_report():
    
    yyyy, mm, dd = map(int, "1996/07/11".split(""))   
    
    age = generator_report(yyyy, mm, dd)
    
    assert age == 26 


