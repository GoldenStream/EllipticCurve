
def decodeLittleEndian(b,bits):
    return sum([b[i] << 8*i for i in range((bits+7)/8)])




                       
    
    
