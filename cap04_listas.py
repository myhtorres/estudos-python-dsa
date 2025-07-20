Trabalhando com Listas

# Criando uma lista
lista_1 = ["arroz, frango, tomate, leite"]

type(lista_1)
list

# Imprimindo a lista
print(lista_1)
['arroz, frango, tomate, leite']

# Criando outra lista
lista_2 = ["arroz", "frango", "tomate", "leite"]

type(lista_2)
list

# Imprimindo a lista
print(lista_2)
['arroz', 'frango', 'tomate', 'leite']

# Criando lista
lista_3 = [23, 100, "Cientista de Dados"]

type(lista_3)
list

# Imprimindo
print(lista_3)
[23, 100, 'Cientista de Dados']

# Atribuindo cada valor da lista a uma variável.
item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

# Imprimindo as variáveis
print(item1, item2, item3)
23 100 Cientista de Dados
Atualizando Um Item da Lista

lista_2
['arroz', 'frango', 'tomate', 'leite']

# Imprimindo um item da lista
lista_2[2]
'tomate'

# Atualizando um item da lista
lista_2[2] = "chocolate"

# Imprimindo lista alterada
lista_2
['arroz', 'frango', 'chocolate', 'leite']
Deletando Um Item da Lista

lista_2
['arroz', 'frango', 'chocolate', 'leite']

# Não é possível deletar um item que não existe na lista. Vai gerar erro index out of range
del lista_2[4]   
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_2727/385579566.py in <module>
      1 # Não é possível deletar um item que não existe na lista. Vai gerar erro index out of range
----> 2 del lista_2[4]

IndexError: list assignment index out of range


# Deletando um item específico da lista
del lista_2[3]

# Imprimindo o item com a lista alterada
lista_2
['arroz', 'frango', 'chocolate']
Listas de Listas (Listas Aninhadas)
Listas de listas são matrizes em Python.

# Criando uma lista de listas
listas = [ [1,2,3], [10,15,14], [10.1,8.7,2.3] ]

# Imprimindo a lista
print(listas)
[[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]

# Atribuindo um item da lista a uma variável
a = listas[0]

a
[1, 2, 3]

b = a[0]

b
1

list1 = listas[1]

list1
[10, 15, 14]

valor_1_0 = list1[0]

valor_1_0
10

valor_1_2 = list1[2]

valor_1_2
14

list2 = listas[2]

list2
[10.1, 8.7, 2.3]

valor_2_0 = list2[0]

valor_2_0
10.1
Operações com Listas

# Criando uma lista aninhada (lista de listas)
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

listas
[[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]

# Atribuindo à variável a o primeiro valor da primeira lista
a = listas[0][0]

a
1

b = listas[1][2]

b
14

c = listas[0][2] + 10

c
13

d = 10

d
10

e = d * listas[2][0]

e
101.0
Concatenando Listas

lista_s1 = [34, 32, 56]

lista_s1
[34, 32, 56]

lista_s2 = [21, 90, 51]

lista_s2
[21, 90, 51]

# Concatenando listas
lista_total = lista_s1 + lista_s2

lista_total
[34, 32, 56, 21, 90, 51]
Operador in

# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]

# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)
False

# Verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)
True
Funções Built-in

# Criando uma lista
lista_numeros = [10, 20, 50, -3.4]

# Função len() retorna o comprimento da lista
len(lista_numeros)
4

# Função max() retorna o valor máximo da lista
max(lista_numeros)
50

# Função min() retorna o valor mínimo da lista
min(lista_numeros)
-3.4

# Criando uma lista
lista_formacoes_dsa = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]

lista_formacoes_dsa
['Analista de Dados', 'Cientista de Dados', 'Engenheiro de Dados']

# Adicionando um item à lista
lista_formacoes_dsa.append("Engenheiro de IA")

lista_formacoes_dsa
['Analista de Dados',
 'Cientista de Dados',
 'Engenheiro de Dados',
 'Engenheiro de IA']

lista_formacoes_dsa.append("Engenheiro de IA")

lista_formacoes_dsa
['Analista de Dados',
 'Cientista de Dados',
 'Engenheiro de Dados',
 'Engenheiro de IA',
 'Engenheiro de IA']

lista_formacoes_dsa.count("Engenheiro de IA")
2

# Criando uma lista vazia
a = []

print(a)
[]

type(a)
list

a.append(10)

a
[10]

a.append(50)

a
[10, 50]

old_list = [1,2,5,10]

new_list = []

# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)

new_list
[1, 2, 5, 10]

cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print (cidades)
['Recife', 'Manaus', 'Salvador', 'Fortaleza', 'Palmas']

cidades.index('Salvador')
2
Lembre-se: em Python o índice começa por 0!

cidades.index('Rio de Janeiro')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_2727/3891498012.py in <module>
----> 1 cidades.index('Rio de Janeiro')

ValueError: 'Rio de Janeiro' is not in list


cidades
['Recife', 'Manaus', 'Salvador', 'Fortaleza', 'Palmas']

cidades.insert(2, 110)

cidades
['Recife', 'Manaus', 110, 'Salvador', 'Fortaleza', 'Palmas']

# Remove um item da lista
cidades.remove(110)

cidades
['Recife', 'Manaus', 'Salvador', 'Fortaleza', 'Palmas']

# Reverte a lista
cidades.reverse()

# Imprime a lista
cidades
['Palmas', 'Fortaleza', 'Salvador', 'Manaus', 'Recife']

x = [3, 4, 2, 1]

x
[3, 4, 2, 1]

# Ordena a lista
x.sort()

x
[1, 2, 3, 4]
Fim
