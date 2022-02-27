#https://tjkendev.github.io/procon-library/python/math/gcd.html

def extended_gcd(a, b):
	if b:
		d, y, x = extended_gcd(b, a%b)
		y -= (a//b) * x
		return d, x, y
	return a, 1, 0