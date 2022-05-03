import math
liczby = input("Aby obliczyć silnię, podaj dwie liczby oddzielone spacją:")
liczby = liczby.split(" ")
def newton(n,k):
	return (math.comb(n, k))