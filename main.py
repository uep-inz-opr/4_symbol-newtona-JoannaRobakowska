import math
liczby = input("Aby obliczyć silnię, podaj dwie liczby oddzielone spacją:")
liczby = liczby.split(" ")
def dwum(n,k):
    wynik=1
    for i in range (1,k):
        wynik=wynik*(n-i+1)/i
    return wynik
 
while(t): 
    n,k=input().split()    
    n=int(n)
    k=int(k)
    print(dwum(n,k))