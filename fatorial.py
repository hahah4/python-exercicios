print('-'*20)
print('Calculo de fatorial.')
print('-'*20)
n = int(input('Digite um número para calcular o fatorial:'))
f=1
for n in range (n,0,-1):
    print(n,'*' if n>1 else '= ', end=''.format(n))
    f*=n
print(f)
    
    
