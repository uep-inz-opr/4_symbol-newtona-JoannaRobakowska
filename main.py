from math import factorial
def silnia(n, k):
	return factorial(n) // (factorial(k) * factorial(n-1))
	print (silnia(6, 4))

#t=int(stdin.readline());
#t = int(input())
 
#for i in range(t):
#	n,k = map(int, input().split())
#	if k == 0 or k == n : print ("1")
#	else : print (silnia(n,k))

#while(t):
	#n,k=input().split()
	#n=int(6)
	#k=int(4)
	#print(silnia(n,k))
#liczby = input("Aby obliczyć silnię, podaj dwie liczby oddzielone spacją:")
#iczby = liczby.split(" ")
#def dwum(n,k):
 ##  for i in range (1,k):
   #     wynik=wynik*(n-i+1)/i
    #return wynik
 
#while(t): 
 #   n,k=input().split()    
  #  n=int(n)
   # k=int(k)
    #print(dwum(n,k))


#    import math
#print ("podaj wartości oddzielone spacją")
#	if a<0 or b<0 or c<0
#	print ("błędne dane")
###		print (wynik)
#	if a=int, b=int, c=0:
#		wynik=a*b
#		print (wynik)
#	if a=int, b=int, c=int:
#		p=(a+b+c)/2
##		print (wynik)


