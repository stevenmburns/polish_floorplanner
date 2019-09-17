
import bisect
import logging
from collections import defaultdict

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
            xpairs = list(zip( self.xs[:-1], self.xs[1:]))
            ypairs = list(zip( self.ys[:-1], self.ys[1:]))

# Check non-decreasing x and non-increasing y
            assert all( r<=s for (r,s) in xpairs)
            assert all( r>=s for (r,s) in ypairs)

#  We don't have a stutter in both dimensions in the same transition

            assert all( not (r == s and u == v) for ((r,s),(u,v)) in zip(xpairs,ypairs))

    def p( self, i):
        return self.xs[i], self.ys[i]

    @staticmethod
    def compute( p0, p1, x, op=min):
        x0, y0 = p0
        x1, y1 = p1

        if x0 == x1:
            assert x == x0, (p0,p1,x)
            return op(y0,y1)
        else:
            return y0 + (y1-y0)/(x1-x0)*(x-x0)

    def __call__(self, x, func=min):
        q = bisect.bisect( self.xs, x)

        if q == 0:
            raise Exception(f"Value out of range: {x} < {self.xs[0]}")
        if q == len(self.xs):
            if x > self.xs[-1]:
                return self.ys[-1]
            else:
                assert x == self.xs[-1]
                if q == 1:
                    return self.ys[0]
                q -= 1

        # special stuttering case
        if q > 1 and  x == self.xs[q-1] and x == self.xs[q-2]:
            q -= 1

        assert q > 0
        return Piecewise.compute( self.p(q-1), self.p(q), x, func)

    def __add__(self, other):

# Assert domain is identical: relax later        

        domain0 = defaultdict(int)
        for x in self.xs:
            domain0[x] += 1
        domain1 = defaultdict(int)
        for x in other.xs:
            domain1[x] += 1

        logging.info( f"Before: {domain0} {domain1}")

        for (k,v) in domain1.items():
            domain0[k] = max( domain0[k], v)

        logging.info( f"After: {domain0} {domain1}")

        points = []
        for (k,v) in sorted(domain0.items()):
            assert v <= 2
            if v == 2:
                points.append( (k, self(k,max) + other(k,max)))
            points.append( (k, self(k) + other(k)))

        return Piecewise( points)
