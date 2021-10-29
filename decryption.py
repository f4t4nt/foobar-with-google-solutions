import base64

msg = "FU4AHQINEV0RT0FRQVUJGxYJFUlYDkULDgcNFw8OBg1GTk4ORQ0SHwQXAwwXT01OU0sEDg4ZFQFJ SUlIRgcaTRANBQIDHgtOX0hGDxdGCw0XDgwXAB1USFtOU1sMBA4IChcKTl9IRhwVTAABFRhGUlRJ VBsACBEJTkhGDQ4dSUlJSEYZHUBDTxw="

key = 'nishant.bhakar'

result = []
for i, c in enumerate(base64.b64decode(msg)):
    result.append(chr(c ^ ord(key[i % len(key)])))

print(''.join(result))