def decodeUCoordinate(u,bits):
    u_list = [ord(b) for b in u]
    # Ignore any unused bits.
    if bits % 8:
        u_list[-1] &= (1<<(bits % 8)) -1
    return decodeLittleEndian(u_list, bits)
