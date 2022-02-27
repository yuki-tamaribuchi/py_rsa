from rsa.rsa import rsa
from crypt.encrypt import encrypt
from crypt.decrypt import decrypt

if __name__ == "__main__":
	p = 11
	q = 5
	e = 3

	public_key, private_key = rsa(p, q, e)
	
	encrypted_data = encrypt("0", public_key)
	print("encrypted_data: ", encrypted_data)
	
	decrypted_data = decrypt(encrypted_data, private_key)
	print("decrypted_data: ", decrypted_data)