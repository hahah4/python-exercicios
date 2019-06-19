#Programa que calcula uma senquência Fibonacci
#Autor: Fabrício Costa.

t0= 0
t1= 1
t2= 2
c=0
print('-'*20)
print('Fibonacci')
print('-'*20)
n = int(input('Digite o número da sequência:'))
for t in range(0,3):
	print(t)
for n in range (2, n):
	t= t1+t2 
	print(t)
	t1= t2                            
	t2 = t
	c+=1
