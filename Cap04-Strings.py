Criando uma String
Para criar uma string em Python você pode usar aspas simples ou duplas. Por exemplo:

# Uma única palavra
'Oi'
'Oi'

# Uma frase
'Criando uma string em Python'
'Criando uma string em Python'

# Podemos usar aspas duplas
"Podemos usar aspas duplas ou simples para strings em Python"
'Podemos usar aspas duplas ou simples para strings em Python'

# Você pode combinar aspas duplas e simples
"Testando strings em 'Python'"
"Testando strings em 'Python'"
Imprimindo uma String

print ('Testando Strings em Python')
Testando Strings em Python

print ('Testando \n Strings \n em \n Python')
Testando 
 Strings 
 em 
 Python

print ('\n')


Indexando Strings

# Atribuindo uma string
s = 'Data Science Academy'

print(s)
Data Science Academy
Indexação em Python começar por zero.

# Primeiro elemento da string
s[0]
'D'

s[1]
'a'

s[2]
't'

s[3]
'a'

s[4]
' '
Podemos usar um : para executar um slicing que faz a leitura de tudo até um ponto designado. Por exemplo:

# Retorna todos os elementos da string, começando pela posição 
# (lembre-se que Python começa a indexação pela posição 0),
# até o fim da string.
s[1:]
'ata Science Academy'

# A string original permanece inalterada
s
'Data Science Academy'

# Retorna tudo até a posição de índice 3
s[:3]
'Dat'

# Retorna tudo até a posição de índice 4
s[:4]
'Data'

# Nós também podemos usar a indexação negativa e ler de trás para frente
s[-1]
'y'

# Retornar tudo, exceto a última letra
s[:-1]
'Data Science Academ'
Nós também podemos usar a notação de índice e fatiar a string em pedaços específicos (o padrão é 1).
Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica a frequência para retornar elementos.

s[::1]
'Data Science Academy'

s[::2]
'Dt cec cdm'

s[::-1]
'ymedacA ecneicS ataD'
Propriedades de Strings

s
'Data Science Academy'

# Alterando um caracter (não é possível alterar um elemento da string)
s[0] = 'x'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_2208/3924084394.py in <module>
      1 # Alterando um caracter (não é possível alterar um elemento da string)
----> 2 s[0] = 'x'

TypeError: 'str' object does not support item assignment


# Concatenando strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
'Data Science Academy é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

print(s)
Data Science Academy é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!

# Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'

letra * 3
'www'
Funções Built-in de Strings

s
'Data Science Academy é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

# Upper Case 
s.upper()
'DATA SCIENCE ACADEMY É A MELHOR MANEIRA DE ESTAR PREPARADO PARA O MERCADO DE TRABALHO EM CIÊNCIA DE DADOS!'

# Lower case
s.lower()
'data science academy é a melhor maneira de estar preparado para o mercado de trabalho em ciência de dados!'

# Dividir uma string por espaços em branco (padrão)
s.split()
['Data',
 'Science',
 'Academy',
 'é',
 'a',
 'melhor',
 'maneira',
 'de',
 'estar',
 'preparado',
 'para',
 'o',
 'mercado',
 'de',
 'trabalho',
 'em',
 'Ciência',
 'de',
 'Dados!']

# Dividir uma string por um elemento específico
s.split('y')
['Data Science Academ',
 ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!']
Funções String

s = 'seja bem vindo ao universo da Linguagem Python!'

s
'seja bem vindo ao universo da Linguagem Python!'

s.capitalize()
'Seja bem vindo ao universo da linguagem python!'

s.count('a')
4

s.isalnum()
False

s.islower()
False

s.isspace()
False

s.endswith('o')
False

s = '1000'

s
'1000'

type(s)
str
Comparando Strings

print("Python" == "R")
False

print("Python" == "Python")
True
Fim
