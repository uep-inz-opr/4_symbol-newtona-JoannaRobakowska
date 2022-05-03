import math
wprowadzenie = int(input("Aby obliczyć silnię, podaj dwie liczby oddzielone spacją:"))
n, k = wprowadzenie.split()
print (math.comb(n, k))