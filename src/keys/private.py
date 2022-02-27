from math.lcm import lcm
from math.extended_gcd import extended_gcd

class PrivateKey:
	def __init__(self, p ,q, e):
		self.n = p * q
		L = lcm(p-1, q-1)
		_, self.d, _ = extended_gcd(e, L)