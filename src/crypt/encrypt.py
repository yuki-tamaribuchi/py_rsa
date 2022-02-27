def encrypt(data, public_key):
	n = public_key.n
	e = public_key.e
	data = ord(data)

	encrypted_data = (data**e) % n
	return encrypted_data