source = "dspttjohuifsvcjdpoabrkttds"


def Shift(word, shift):
    input = [l for l in word]
    for i in range(len(input)):
        hex = ord(input[i])
        hex += shift
        if(hex > 122):
            hex -= 26
        input[i] = chr(hex)
    return "".join(input)

for i in range(26):
    print(Shift(source, i))