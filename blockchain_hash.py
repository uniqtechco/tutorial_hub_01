#basic hash function example turns the word 'anders' into a hash
# inspired by ethereum org recommendation Anders Brownworth youtube

import hashlib
m = hashlib.sha256()
m.update(b"anders")
m.digest() #b'\x19\xeaJ\xc2\xe1\xa5;\x12g\xfeZa\xa3\xb6\xb8\x1fv\x0c\xe4":%\xb4\x95\xa5\xe2\xb6\x18=\xa6\x87\x17https://github.com/uniqtechco/tutorial_hub_01'
m.hexdigest() #19ea4ac2e1a53b1267fe5a61a3b6b81f760ce4223a25b495a5e2b6183da68717
# the hexdigest() is a more familiar looking format
# any simple change will drastically change the output
m.update(b"anders ") #I just added a space here.
m.hexdigest() #a51179cda3e63b7358246b60f71bc73cb61bd5ccd702c0f846edee6459b2ca36
