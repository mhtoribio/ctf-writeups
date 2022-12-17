def bitsToByte(bits):
    byte = 0
    for i, b in enumerate(bits):
        byte |= b << i
    return byte

def decode(s):
    outbits  = [int(s[7-i]) for i in range(0,8)]
    inbits = [0 for i in range(8)]
    inbits[0] = 1 if outbits[7] == outbits[0] else 0
    inbits[1] = outbits[1] if outbits[3] else outbits[2]
    inbits[2] = outbits[3]
    inbits[3] = outbits[4] ^ outbits[5] ^ outbits[6]
    inbits[4] = outbits[5] ^ outbits[6]
    inbits[5] = 1 if not outbits[6] else 0
    inbits[6] = outbits[7]
    inbits[7] = 0
    return chr(bitsToByte(inbits))

with open("output.txt", "r") as f:
    ls = f.readlines()

ls = list(map(lambda x: x.strip(), ls))
output = list(map(lambda l: decode(l), ls))
output = "".join(output)
print(output)
