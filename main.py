import math
print ("Aby obliczyć silnię, podaj dwie liczby oddzielone spacją:")
    def dwumianREK(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return float(n)*dwumianRek(n-1,k-1)/k