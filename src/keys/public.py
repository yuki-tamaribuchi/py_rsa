class PublicKey:
	def __init__(self, p, q, e):
		self.n = p * q
		self.e = e