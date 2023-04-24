import hashlib
m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m.update(b"Hello It's me")
print(m.hexdigest())
