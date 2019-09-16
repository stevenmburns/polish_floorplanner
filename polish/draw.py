
from . import Tree, Trans

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def set_trans( t, wh_tbl):
    def aux( obj):
       if isinstance( obj, Tree):
            lb = aux( obj.l)
            rb = aux( obj.r)
            if obj.op == '|':
                obj.l_tr = Trans(ox=0,oy=max(0,(rb[3] - lb[3])/2))
                obj.r_tr = Trans(ox=lb[2],oy=max(0,(lb[3] - rb[3])/2))
                bbox = [0,0,lb[2]+rb[2],max(lb[3],rb[3])]
            else:
                assert obj.op == '-'
                obj.l_tr = Trans(ox=max(0,(rb[2] - lb[2])/2),oy=0)
                obj.r_tr = Trans(ox=max(0,(lb[2] - rb[2])/2),oy=lb[3])
                bbox = [0,0,max(lb[2],rb[2]),lb[3]+rb[3]]
            return bbox
       else:
           (w,h) = wh_tbl[obj] if obj in wh_tbl else (1,1)
           bbox = [0,0,w,h]
           return bbox
    bbox = aux( t)
    return bbox

def gen_tbl( t, wh_tbl): 
    tbl = {}
    def aux( obj, tr):
       if isinstance( obj, Tree):
           lb = aux( obj.l, tr.postMult( obj.l_tr))
           rb = aux( obj.r, tr.postMult( obj.r_tr))
       else:
           (w,h) = wh_tbl[obj] if obj in wh_tbl else (1,1)
           ll = tr.hit( (0,0))
           ur = tr.hit( (w,h))
           tbl[obj] = [ ll[0], ll[1], ur[0], ur[1]]
    aux( t, Trans())
    return tbl

def render_with_trans( t, wh_tbl):
    bbox = set_trans( t, wh_tbl)
    tbl = gen_tbl( t, wh_tbl)
    return (tbl,bbox)

def render( tr, wh_tbl):
    tbl = {}
    def aux( obj, x, y):
       if isinstance( obj, Tree):
            lb = aux( obj.l, x, y)
            if obj.op == '|':
                rb = aux( obj.r, lb[2], y)
            else:
                assert obj.op == '-'
                rb = aux( obj.r, x, lb[3])
            return [x,y,max(lb[2],rb[2]),max(lb[3],rb[3])]
       else:
           (w,h) = wh_tbl[obj] if obj in wh_tbl else (1,1)
           r = [x,y,x+w,y+h]
           tbl[obj] = r
           return r
    bbox = aux( tr, 0, 0)
    return (tbl,bbox)


def draw(rects, bbox):

    brd = 0.05

    fig,ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set( xlim=(bbox[0]-brd,bbox[2]+brd), ylim=(bbox[1]-brd,bbox[3]+brd))

    for (idx,r) in rects.items():
        ax.add_patch(Rectangle((r[0], r[1]), r[2]-r[0], r[3]-r[1], alpha=1, fill=None))
        cX, cY = (r[0]+r[2])/2, (r[1]+r[3])/2
        plt.text( cX, cY, str(idx), ha="center", va="center")
    

    plt.show()
