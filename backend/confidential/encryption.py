import hashlib


class Encryptor:
    def __init__(self, text: str):
        self.text = text

    def encrypt(self) -> str:
        bytes_to_hash = self.text.encode("utf-8")
        sha256_hash = hashlib.sha256()
        sha256_hash.update(bytes_to_hash)
        hex_hash = sha256_hash.hexdigest()
        return hex_hash
