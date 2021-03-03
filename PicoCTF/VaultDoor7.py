hexbytes = [0 for i in range(32)]

input = [1096770097
        ,1952395366
        ,1600270708
        ,1601398833
        ,1716808014
        ,1734291511
        ,960049251
        ,1681089078]

for i in range(len(input)):
    item = input[i]
    hexbytes[i*4] = chr((item) >> 24)
    hexbytes[i*4+1] = chr((item & (255 << 16)) >> 16)
    hexbytes[i*4+2] = chr((item & (255 << 8)) >> 8) 
    hexbytes[i*4+3] = chr(item & 255)

print("".join(hexbytes))