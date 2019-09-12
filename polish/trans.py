
class Trans:
    def __init__(self, *, ox=0, oy=0, sx=1, sy=1):
        self.ox = ox
        self.oy = oy
        self.sx = sx
        self.sy = sy

    def hit(self, p):
        """
        sx 0  ox     x    sx*x + ox
        0  sy oy  X  y =  sy*y + oy
        0  0  1      1    1
        """
        x,y = p
        return self.sx*x + self.ox, self.sy*y + self.oy
        
    @staticmethod
    def canonicalRect( r):
        r[0],r[2] = min(r[0],r[2]),max(r[0],r[2])
        r[1],r[3] = min(r[1],r[3]),max(r[1],r[3])
        return r

    def hitRect(self, r):
        ll = self.hit( (r[0],r[1]))
        ur = self.hit( (r[2],r[3]))
        return Trans.canonicalRect(list(ll) + list(ur))
        
    @staticmethod
    def mult(A, B):
        """
        sx 0  ox     Sx 0  Ox     sx*Sx 0     sx*Ox+ox
        0  sy oy  X  0  Sy Oy  =  0     sy*Sy sy*Oy+oy
        0  0  1      0  0  1      0     0     1
        """
        return Trans( sx=A.sx*B.sx,      sy=A.sy*B.sy,
                      ox=A.sx*B.ox+A.ox, oy=A.sy*B.oy+A.oy)
        
    def preMult( self, other):
        return Trans.mult( other, self)

    def postMult( self, other):
        return Trans.mult( self, other)
