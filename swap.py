import mask

def cswap(swap, x_2, x_3):
    dummy = mask(swap) AND (x_2 XOR x_3)
    x_2 = x_2 XOR dummy
    x_3 = x_3 XOR dummy
    return (x_2, x_3)


    
