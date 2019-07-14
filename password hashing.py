import hashlib

str="Jamie Lanister"

print("SHA256")
result= hashlib.sha256(str.encode())
print(result.hexdigest())
print(result)

print("SHA384")
result1=hashlib.sha384(str.encode())
print(result1.hexdigest())
print(result)

print("SHA1")
result2=hashlib.sha1(str.encode())
print(result2.hexdigest())
print(result2)

print("SHA512")
result2=hashlib.sha512(str.encode())
print(result2.hexdigest())
print(result2)

print("md5")
result2=hashlib.md5(str.encode())
print(result2.hexdigest())
print(result2)

print("SHA224")
result2=hashlib.sha224(str.encode())
print(result2.hexdigest())
print(result2)
