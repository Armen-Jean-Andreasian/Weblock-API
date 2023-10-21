from API.backend.confidential.encryption import Encryptor


def main(text):
    return Encryptor(text).encrypt()


assert main('freedom') == '13b1f7ec5beaefc781e43a3b344371cd49923a8a05edd71844b92f56f6a08d38'
assert main('ice-cream') == '34c5ac5923489f2e7b5ab85f0989a8bb7dde45c7f3e45003ec538f61b2e9ac69'
assert main('crayon') == 'd8b1858e24ae617677d50392c61e0ca351d1ef9bcbe683ba71bd4926df6b8fbe'
assert main('icecream') == '4a07a4310034102668a862f2ec7d3ba7416937b2f85c90b38257cf5b13093b0c'
