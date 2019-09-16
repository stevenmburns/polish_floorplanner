
import pytest

from polish import Piecewise

def test_piecewise_empty():
    with pytest.raises(Exception):
        pw = Piecewise()

def test_piecewise_hyperbola():

    pw = Piecewise( [ (0.5,2), (1,1), (2,0.5)])

    with pytest.raises(Exception): 
        assert pw(  0)   == 3

    assert pw( 0.5)  == 2
    assert pw(  1) == 1
    assert pw( 1.5)  == .75
    assert pw(  2) == 0.5

    assert pw( 2.5)  == 0.5

def test_piecewise_vertical():

    pw = Piecewise( [ (0.5,2), (0.5,1), (2,1)])

    assert pw( 0.5)  == 1
    assert pw(  1) == 1
    assert pw( 1.5)  == 1
    assert pw(  2) == 1

    assert pw( 2.5)  == 1

def test_piecewise_sum():

    pwA = Piecewise( [ (0.5,2), (1,1), (2,0.5)])
    pwB = Piecewise( [ (0.5,2), (1,1.5), (2,0.5)])

    pw = pwA + pwB

    assert pw( 0.5)  == 4
    assert pw(  1) == 2.5
    assert pw( 1.5)  == 1.75
    assert pw(  2) == 1

    assert pw( 2.5)  == 1

def test_piecewise_sum_irregular():

    pwA = Piecewise( [ (0.5,2), (.9,1), (2,0.5)])
    pwB = Piecewise( [ (0.5,2), (1.1,1.5), (2,0.5)])

    with pytest.raises(AssertionError):
        pw = pwA + pwB



