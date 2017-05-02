import decodelittleendian

def decodeScalar448(k):
    k_list = [orb(b) for b in k]
    k_list[0] &= 252
    k_list[55] |= 128
    return decodeLittleEndian(k_list, 448)
    
