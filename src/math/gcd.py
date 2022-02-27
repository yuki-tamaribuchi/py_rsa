def gcd(a, b):

	"""
	2以上が返った時は最大公約数。
	1が返った時は互いに素(Coprime)。
	"""

	if a == 0:
		return b
	else:
		return gcd(b%a, a)