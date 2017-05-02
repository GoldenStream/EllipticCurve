import ellipticcurve
import gf

def findCurve(prime, curveCofactor, twistCofactor):
    F = GF(prime)

    for A in xrange(1, 1e9):
        if (A-2) % 4 != 0:
          continue

        try:
          E = EllipticCurve(F, [0, A, 0, 1, 0])
        except:
          continue

        order = E.order()
        twistOrder = 2*(prime+1)-order

        if (order % curveCofactor == 0 and is_prime(order // curveCofactor) and
            twistOrder % twistCofactor == 0 and is_prime(twistOrder // twistCofactor)):
            return A

