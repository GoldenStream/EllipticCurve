def is_prime(n):
  if n < 2:
      return False
  for i in xrange(2, int(n**0.5+1)):
    if n%i == 0:
      return False
  return True

def is_square(n):

    
    return True;
