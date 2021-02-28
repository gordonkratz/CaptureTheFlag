import base64

input = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2"

def decryptFromBase64(s):
    return base64.b64decode(s)

def decryptFromUrlEncode(s):
    result = []
    for i in range(0, len(s) // 3 * 3, 3):
        stri = chr(s[i+1]) + chr(s[i+2])
        num = int(stri, 16)

        result.append(chr(num))
    return "".join(result)

answer = decryptFromBase64(input)
print(answer)
answer = decryptFromUrlEncode(answer)
print("picoCTF{"+answer+"}")