
import bisect

#
# We'll assume there is a vertical line at p(0), and a horizontal line at p(-1)
#
#     |
#     |
#     |
#     0-------1
#             |
#             |
#             |
#             2-------
#
# We can describe indiviual points like this.
#
#

class Piecewise:
    def __init__(self, points):
        self.xs = [ p[0] for p in points]
        self.ys = [ p[1] for p in points]

# Check that we do not have move than one stutter in a row
        if len(self.xs) > 2:
            triples = zip( self.xs[:-2], self.xs[1:-1], self.xs[2:])
            for (r,s,t) in triples:
                assert not (r == s == t)

        if len(self.xs) > 1:
            xpairs = zip( self.xs[:-1], self.xs[1:])
            ypairs = zip( self.ys[:-1], self.ys[1:])

# Check non-decreasing x and non-increasing y
            assert all( r<=s for (r,s) in xpairs)
            assert all( r>=s for (r,s) in ypairs)

#  We don't have a stutter in both dimensions in the same transition
            assert all( not (r == s and u == v) for ((r,s),(u,v)) in zip(xpairs,ypairs))


    def p( self, i):
        return self.xs[i], self.ys[i]

    @staticmethod
    def compute( p0, p1, x):
        x0, y0 = p0
        x1, y1 = p1

        if x0 == x1:
            assert x == x0, (p0,p1,x)
            return y1
        else:
            return y0 + (y1-y0)/(x1-x0)*(x-x0)

    def __call__(self, x):
        q = bisect.bisect( self.xs, x)

        if q == 0:
            raise Exception(f"Value out of range: {x} < {self.xs[0]}")
        if q == len(self.xs):
            return self.ys[-1]

        return Piecewise.compute( self.p(q-1), self.p(q), x)

    def __add__(self, other):

# Assert domain is identical: relax later        

        assert self.xs == other.xs

        points = [ (u,r+s) for (u,r,s) in zip( self.xs, self.ys, other.ys)]
            
        return Piecewise( points)
