__coder__ = "KhodeXenon[Amin]"
__email_ = "Khodexenon@gmail.com"
# This tool is a seperate tool for see its repository in the github go to following link :
link = "https://github.com/KhodeXenon/hash-generator"

import hashlib

class HashTool():
    def __init__(self ,hash):
        self.hash = hash.encode()

    def md5_encrypt(self):
        my_hash = hashlib.md5()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha256_encrypt(self):
        my_hash = hashlib.sha256()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha512_encrypt(self):
        my_hash = hashlib.sha512()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha3_256_encrypt(self):
        my_hash = hashlib.sha3_256()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha3_384_encrypt(self):
        my_hash = hashlib.sha3_384()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha3_224_encrypt(self):
        my_hash = hashlib.sha3_224()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha3_512_encrypt(self):
        my_hash = hashlib.sha3_512()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha1_encrypt(self):
        my_hash = hashlib.sha1()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha384_encrypt(self):
        my_hash = hashlib.sha3_384()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

    def sha224_encrypt(self):
        my_hash = hashlib.sha224()
        my_hash.update(self.hash)
        return my_hash.hexdigest()

