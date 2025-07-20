Funções

print('Hello World')
Hello World

# Definindo uma função
def primeiraFunc():
    print('Hello World')

primeiraFunc()
Hello World

# Definindo uma função
def primeiraFunc():
    nome = 'Bob'
    print('Hello %s' %(nome))

primeiraFunc()
Hello Bob

# Definindo uma função com parâmetro
def segundaFunc(nome):
    print('Hello %s' %(nome))

segundaFunc('Aluno')
Hello Aluno

segundaFunc()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_5033/494153477.py in <module>
----> 1 segundaFunc()

TypeError: segundaFunc() missing 1 required positional argument: 'nome'


# Função para imprimir números
def imprimeNumeros():
    
    # Loop
    for i in range(0, 5):
        print("Número " + str(i))

imprimeNumeros()
Número 0
Número 1
Número 2
Número 3
Número 4

# Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

# Chamando a função e passando parâmetros
addNum(4, 7)
Primeiro número: 4
Segundo número: 7
Soma:  11

# Chamando a função e passando parâmetros
addNum(45, 3)
Primeiro número: 45
Segundo número: 3
Soma:  48

# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
    
   # Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;

# Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)
O parâmetro passado foi:  10

printVarInfo('Chocolate', 'Morango')
O parâmetro passado foi:  Chocolate
O parâmetro passado foi:  Morango

printVarInfo('Data', 'Science', 'Academy')
O parâmetro passado foi:  Data
O parâmetro passado foi:  Science
O parâmetro passado foi:  Academy
Escopo de Variável - Local e Global

# Variável Global
var_global = 10  # Esta é uma variável global
​
# Função
def multiplica_numeros(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiplica_numeros(5, 25)
125

print(var_global)
10

# Variável Global
var_global = 10  # Esta é uma variável global
​
# Função
def multiplica_numeros(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)

multiplica_numeros(5, 25)
125

print(var_local)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_5033/1392635205.py in <module>
----> 1 print(var_local)

NameError: name 'var_local' is not defined


print(var_global)
10
Funções Built-in

abs(-56)
56

abs(23)
23

bool(0)
False

bool(1)
True

int(4.3)
4

str(13)
'13'

float(5)
5.0

# Erro ao executar por causa da conversão
idade = input("Digite sua idade: ")
if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  
Digite sua idade: 14
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_5033/1920333143.py in <module>
      1 # Erro ao executar por causa da conversão
      2 idade = input("Digite sua idade: ")
----> 3 if idade > 13:
      4     print("Você pode acessar Redes Sociais sem supervisão!")
      5 else:

TypeError: '>' not supported between instances of 'str' and 'int'


# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  
Digite sua idade: 12
Seus pais não deveriam você acessar Redes Sociais sem supervisão!

int("26")
26

float("123.345")
123.345

float("123.3A45")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_5033/1294861840.py in <module>
----> 1 float("123.3A45")

ValueError: could not convert string to float: '123.3A45'


str(14)
'14'

len([23,34,45,46])
4

array = [1, 2, 3]

max(array)
3

min(array)
1

list1 = [16, 23, 44, 75]

sum(list1)
158
Criando Funções Usando Outras Funções
https://pypi.org/

import math
​
# Verificando se um número é primo
def numPrimo(num):
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

numPrimo(541)
'Este número é primo'

numPrimo(2)
'Este número é primo'

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)

lowercased_string
'este texto deveria estar todo em lowercase'
Fazendo Split dos Dados

# Fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados."

# Isso divide a string em uma lista de palavras
print(split_string_palavras(texto))
['Esta', 'função', 'será', 'bastante', 'útil', 'para', 'separar', 'grandes', 'volumes', 'de', 'dados.']

# Podemos atribuir o output de uma função para uma variável
token = split_string_palavras(texto)

token
['Esta',
 'função',
 'será',
 'bastante',
 'útil',
 'para',
 'separar',
 'grandes',
 'volumes',
 'de',
 'dados.']

# Fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

split_string_letras(texto)
E
S
T
A
 
F
U
N
Ç
Ã
O
 
S
E
R
Á
 
B
A
S
T
A
N
T
E
 
Ú
T
I
L
 
P
A
R
A
 
S
E
P
A
R
A
R
 
G
R
A
N
D
E
S
 
V
O
L
U
M
E
S
 
D
E
 
D
A
D
O
S
.
Fim
