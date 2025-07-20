Função Range

# Imprimindo números de 1 a10
for i in range(1, 11):
    print(i)
1
2
3
4
5
6
7
8
9
10

# Imprimindo números pares entre 50 e 101
for i in range(50, 101, 2):
    print(i)
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

# Imprimindo os números pares negativos entre 0 e -20
for i in range(0, -20, -2):
    print(i)
0
-2
-4
-6
-8
-10
-12
-14
-16
-18

# Usando o tamanho de uma lista na função range()
lista = ['Abacaxi', 'Banana', 'Morango', 'Uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i])
Abacaxi
Banana
Morango
Uva
Fim
