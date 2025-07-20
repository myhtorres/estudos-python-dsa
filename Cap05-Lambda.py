Expressão Lambda

# Definindo uma função - 3 linhas de código
def potencia(num):
    resultado = num ** 2
    return resultado

potencia(5)
25

# Definindo uma função - 2 linhas de código
def potencia(num):
    return num ** 2

potencia(5)
25

# Definindo uma função - 1 linha de código
def potencia(num): return num ** 2

potencia(5)
25

# Definindo uma expressão lambda (função anônima)
potencia = lambda num: num ** 2

potencia(5)
25

# Lembre: operadores de comparação retornam boolean: true or false
Par = lambda x: x%2==0

Par(3)
False

Par(4)
True

first = lambda s: s[0]

first('Python')
'P'

reverso = lambda s: s[::-1]

reverso('Python')
'nohtyP'

addNum = lambda x,y : x+y

addNum(2,3)
5
Fim
