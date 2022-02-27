def decrypt(data, private_key):
	d = private_key.d
	n = private_key.n

	decrypted_data = (data**d) % n
	return chr(decrypted_data)