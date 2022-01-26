print(ord('a'))
print(chr(72))

strNew = "hello"

enc_asci = strNew.encode('ascii')
enc_utf8 = strNew.encode('utf8')
enc_utf16 = strNew.encode('utf16')

print(type(enc_asci))
print(enc_asci)
print(enc_utf8)
print(enc_utf16)

print(len(enc_asci))
print(len(enc_utf8))
print(len(enc_utf16))

ba = bytearray(b'hello')
ba[0] = 87
print(ba)

jpeg = [1, 2, 3, 5, 7, 8, 10]
print(type(jpeg))


