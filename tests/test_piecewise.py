
import pytest

from polish import Piecewise

def test_piecewise_empty():
    with pytest.raises(Exception):
        Piecewise()

def test_piecewise_hyperbola():

    pw = Piecewise( [ (0.5,2), (1,1), (2,0.5)])

    with pytest.raises(Exception): 
        pw(  0)

    assert pw( 0.5)  == 2
    assert pw(  1) == 1
    assert pw( 1.5)  == .75
    assert pw(  2) == 0.5

    assert pw( 2.5)  == 0.5

def test_piecewise_discrete():

    pw = Piecewise( [ (1,2), (2,2), (2,1)])

    with pytest.raises(Exception): 
        pw(  0.5)

    assert pw(  1)   == 2
    assert pw(  1.5) == 2
    assert pw(  2)   == 1
    assert pw(  3)   == 1

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

    pw = pwA + pwB

    assert pw( 0.5) == 4
    assert abs( pw( 0.9) - 2.6666667) < 0.0001
    assert abs( pw( 1.1) - 2.4090909) < 0.0001

def test_piecewise_sum_irregular2():

    pwA = Piecewise( [ (1,2), (2,2), (2,1)])
    pwB = Piecewise( [ (1,2), (2,2), (2,1)])

    pw = pwA + pwB

    assert pw( 1) == 4
    assert pw( 1.99) == 4
    assert pw( 2) == 2
    assert pw( 2.01) == 2
    assert pw( 3) == 2

def test_piecewise_single_point():
    pw = Piecewise( [ (1,1)])
    assert pw( 1) == 1
    assert pw( 1.01) == 1
    with pytest.raises(Exception):
        pw( 0.09)

def test_piecewise_sum_irregular3():

    pwA = Piecewise( [ (1,2), (2,2), (2,1)])
    pwB = Piecewise( [ (1,2), (1.5,2), (1.5,1), (2,1)])

    assert pwB( 1.5, min) == 1
    assert pwB( 1.51, min) == 1


    assert pwA( 1.5, max) == 2
    assert pwB( 1.5, max) == 2
    assert pwB( 1.51, max) == 1


    pw = pwA + pwB

    assert pw( 1) == 4
    assert pw( 1.49) == 4
    assert pw( 1.50) == 3
    assert pw( 1.51) == 3

    assert pw( 3) == 2
