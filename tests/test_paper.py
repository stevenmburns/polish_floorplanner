import pytest
from polish import *

#
# Only fixed orientations ($S_2$ is empty)
#
def test_A():
#    problem = [( 10, 0.4, 2.5), (10, 0.4, 2.5), (10, 0.4, 2.5)]
#    connections = { (0,1): 1, (1,2): 1}

    print(build_tree([ 0, 1, "|", 2, "-"]))

    with pytest.raises( AssertionError): # more than one on stack at end
        print(build_tree([ 0, 1, "|", 2, "-", 3]))

    with pytest.raises( IndexError): # more operators than leaves
        print(build_tree([ 0, 1, "|", "-"]))

def test_fig_1b():
    tr =  build_tree([1,6,'-',3,5,'|',2,'-',7,4,'-','|','|'])
    print(tr)
    tbl, bbox = render(tr, {})
    print(tbl)
    print(bbox)



def test_render():
    wh_tbl = { 6: (1,2), 2: (2,1.5), 3: (1,1.5)}

    tr =  build_tree([1,6,'-',3,5,'|',2,'-',7,4,'-','|','|'])
    print(tr)
    tbl, bbox = render(tr, wh_tbl)
    draw( tbl, bbox)

def test_render_with_trans():
    wh_tbl = { 6: (1,2), 2: (2,1.5), 3: (1,1.5)}

    tr =  build_tree([1,6,'-',3,5,'|',2,'-',7,4,'-','|','|'])
    print(tr)
    tbl, bbox = render_with_trans( tr, wh_tbl)
    draw( tbl, bbox)

from itertools import product
def test_draw_rects():
    N = 8
    rects = {}
    for (idx,(x,y)) in enumerate(product( range(N), range(N))):
        rects[idx] = [x,y,x+1,y+1]
    draw( rects, [0,0,N,N])
