Loop For

# Criando uma tupla e imprimindo cada um dos valores
tp = (2,3,4)
for i in tp:
    print(i)
2
3
4

# Criando uma lista e imprimindo cada um dos valores
ListaDeStrings = ["Data", "Science", "Academy"]
for i in ListaDeStrings:
    print(i)
Data
Science
Academy

# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for contador in range(0,5):
    print(contador)
0
1
2
3
4

# Imprimindo os números pares da lista de números
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print (num)
2
4
6
8
10

# Listando os números no intervalo entre 0 e 101, com incremento em 2
for i in range(0,101,2):  
    print(i)
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100

# Strings também são sequências
for caracter in 'Python é uma linguagem de programação divertida!':
    print (caracter)
P
y
t
h
o
n
 
é
 
u
m
a
 
l
i
n
g
u
a
g
e
m
 
d
e
 
p
r
o
g
r
a
m
a
ç
ã
o
 
d
i
v
e
r
t
i
d
a
!
Loop For Aninhado

# Loops aninhados
​
lista1 = [0,1,2,3,4]
lista2 = [1,2,3]
​
# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno
    for elemento_lista2 in lista2:
        
        print('\n', elemento_lista1 * elemento_lista2)
        
    print('----')

 0

 0

 0
----

 1

 2

 3
----

 2

 4

 6
----

 3

 6

 9
----

 4

 8

 12
----

# O número 47 aparece nas duas listas?
​
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
​
# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno
    for elemento_lista2 in lista2:
        
        # Condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            
            print("O número 47 foi encontrado nas duas listas!")
O número 47 foi encontrado nas duas listas!

# Some os números pares da primeira lista com os números pares da segunda lista
​
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0
​
# Loop externo
for lista in [lista1, lista2]:
    
    # Loop interno
    for num in lista:
        
        # Condicional
        if num % 2 == 0:
            soma += num
            
print("O soma dos números pares das duas listas é igual a", soma)
O soma dos números pares das duas listas é igual a 170

# Listas podem ser concatenadas em Python
lista1 + lista2
[10, 16, 24, 39, 47, 32, 89, 47, 76, 12]

# Some os números pares da primeira lista com os números pares da segunda lista
​
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0
​
for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num
​
print("Soma dos valores pares:", soma)
Soma dos valores pares: 170

# Loop em lista de listas (matrizes) para encontrar o maior número
​
matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior_numero = 0
​
# Loop externo
for linha in matriz:
    
    # Loop interno
    for num in linha:
        
        # Condicional
        if num > maior_numero:
            maior_numero = num
​
print("Maior número:", maior_numero)
Maior número: 215

# Listando as chaves de um dicionário
dict = {'k1':'Python','k2':'R','k3':'Scala'}
for item in dict:
    print(item)
k1
k2
k3

# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k,v in dict.items():
    print (k,v)
k1 Python
k2 R
k3 Scala
Fim
