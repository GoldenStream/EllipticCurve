import ellipticcurve
import gf

def findBasepoint(prime, A):
       '''F和E是函数对象'''
       F = GF(prime)
       E = EllipticCurve(F, [0, A, 0, 1, 0])

       for uInt in range(1, 1e3):
         u = F(uInt)
         v2 = u^3 + A*u^2 + u
         if not v2.is_square():
           continue
         v = v2.sqrt()

         point = E(u, v)
         order = point.order()
         if order > 8 and order.is_prime():
       return point
