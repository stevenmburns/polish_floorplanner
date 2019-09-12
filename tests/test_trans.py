import pytest
from polish import *

def test_hit():
    A = Trans()

    assert A.hit( (0,0)) == (0,0)
    
    A = Trans( ox=10, oy=-10)

    assert A.hit( (0,0)) == (10,-10)    

    assert A.hit( (-10,10)) == (0,0)    

    A = Trans( sx=-1)

    assert A.hit( (-10,10)) == (10,10)    

    A = Trans( sy=-1)

    assert A.hit( (-10,10)) == (-10,-10)    

def test_hitRect():
    A = Trans( ox=10, oy=-10)
    assert A.hitRect( [0,0,1,1]) == [10,-10,11,-9]

    A = Trans( ox=10, oy=-10, sx=-1)
    assert A.hitRect( [0,0,1,1]) == [9,-10,10,-9]

def test_mult():
    A = Trans()
    B = Trans()
    C= A.preMult( B)

    assert C.hit( (0,0)) == (0,0)
    assert C.hit( (1,1)) == (1,1)

    A = Trans( ox=10)
    B = Trans()
    C= A.preMult( B)

    assert C.hit( (0,0)) == (10,0)
    assert C.hit( (1,1)) == (11,1)

    A = Trans( ox=10)
    B = Trans( oy=10)
    C= A.preMult( B)

    assert C.hit( (0,0)) == (10,10)
    assert C.hit( (1,1)) == (11,11)

    A = Trans( sx=-1)
    B = Trans( sx=-1)
    C= A.preMult( B)

    assert C.hit( (0,0)) == (0,0)
    assert C.hit( (1,1)) == (1,1)

    A = Trans( ox=10)
    B = Trans( sx=-1)
    C= A.preMult( B)

    assert C.hit( (0,0)) == (-10,0)
    assert C.hit( (1,1)) == (-11,1)

    A = Trans( ox=10)
    B = Trans( sx=-1)
    C= B.postMult( A)

    assert C.hit( (0,0)) == (-10,0)
    assert C.hit( (1,1)) == (-11,1)

    A = Trans( ox=10)
    B = Trans( sx=-1)
    C= A.postMult( B)

    assert C.hit( (0,0)) == (10,0)
    assert C.hit( (1,1)) == ( 9,1)
