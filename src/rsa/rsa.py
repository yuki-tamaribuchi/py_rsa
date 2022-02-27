from keys.public import PublicKey
from keys.private import PrivateKey

def rsa(p, q, e):
	"""
	ed ≡ 1 mod (p-1)(q-1)

	eとnが公開鍵、dが秘密鍵になる。

	eは(p-1)(q-1)と互いに素になる値で、(p-1)(q-1)より小さい値。


	"""
	n = p * q

	public_key = PublicKey(p, q, e)
	private_key = PrivateKey(p, q, e)

	return public_key, private_key