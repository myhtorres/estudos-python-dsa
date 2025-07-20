Trabalhando com Tuplas

# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')

# Imprimindo a tupla
tupla1
('Geografia', 23, 'Elefantes', 9.8, 'Python')

# Tuplas não suportam append()
tupla1.append("Chocolate")   
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_3083/2593053863.py in <module>
      1 # Tuplas não suportam append()
----> 2 tupla1.append("Chocolate")

AttributeError: 'tuple' object has no attribute 'append'


# Tuplas não suportam delete de um item específico
del tupla1["Elefantes"]  
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_3083/3644285831.py in <module>
      1 # Tuplas não suportam delete de um item específico
----> 2 del tupla1["Elefantes"]

TypeError: 'tuple' object does not support item deletion


# Tuplas podem ter um único item
tupla1 = ("Chocolate")

tupla1
'Chocolate'

tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')

tupla1[0]
'Geografia'

# Verificando o comprimento da tupla
len(tupla1)
5

# Slicing, da mesma forma que se faz com listas
tupla1[1:]
(23, 'Elefantes', 9.8, 'Python')

tupla1.index('Elefantes')
2

# Tuplas não suportam atribuição de item
tupla1[1] = 21
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_3083/885633849.py in <module>
      1 # Tuplas não suportam atribuição de item
----> 2 tupla1[1] = 21

TypeError: 'tuple' object does not support item assignment


# Deletando a tupla
del tupla1

tupla1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_3083/3141490790.py in <module>
----> 1 tupla1

NameError: name 'tupla1' is not defined


# Criando uma tupla
t2 = ('A', 'B', 'C')

t2
('A', 'B', 'C')

# Tuplas não suportam atribuição de item
t2[0] = 'D'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_3083/430084819.py in <module>
      1 # Tuplas não suportam atribuição de item
----> 2 t2[0] = 'D'

TypeError: 'tuple' object does not support item assignment


# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)

type(t2)
tuple

type(lista_t2)
list

lista_t2
['A', 'B', 'C']

lista_t2.append('D')

# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)

t2
('A', 'B', 'C', 'D')
Fim
