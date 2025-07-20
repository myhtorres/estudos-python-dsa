Trabalhando com Variáveis

# Atribuindo o valor 1 à variável var_teste
var_teste = 1

# Imprimindo o valor da variável
var_teste
1

# Imprimindo o valor da variável
print(var_teste)
1

# Não podemos utilizar uma variável que não foi definida. Leia a mensagem de erro.
my_var
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Input In [5], in <cell line: 2>()
      1 # Não podemos utilizar uma variável que não foi definida. Leia a mensagem de erro.
----> 2 my_var

NameError: name 'my_var' is not defined


var_teste = 2

var_teste
2

type(var_teste)
int

var_teste = 9.5

type(var_teste)
float

x = 1

x
1
Declaração Múltipla

pessoa1, pessoa2, pessoa3 = "Bob", "Maria", "Ana"

pessoa1
'Bob'

pessoa2
'Maria'

pessoa3
'Ana'

fruta1 = fruta2 = fruta3 = "Melancia"

fruta1
'Melancia'

fruta2
'Melancia'

fruta3
'Melancia'

# Fique atento!!! Python é case-sensitive. Criamos a variável fruta2, mas não a variável Fruta2.
# Letras maiúsculas e minúsculas tem diferença no nome da variável.
Fruta2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Input In [21], in <cell line: 3>()
      1 # Fique atento!!! Python é case-sensitive. Criamos a variável fruta2, mas não a variável Fruta2.
      2 # Letras maiúsculas e minúsculas tem diferença no nome da variável.
----> 3 Fruta2

NameError: name 'Fruta2' is not defined

Pode-se usar letras, números e underline em nome de variável (mas não se pode começar com números).

x1 = 50

x1
50

# Mensagem de erro, pois a linguagem Python não permite nomes de variáveis que iniciem com números
1x = 50
  Input In [24]
    1x = 50
     ^
SyntaxError: invalid syntax


Não se pode usar palavras reservadas como nome de variável
False
class
finally
is
return
None
continue
for
lambda
try
True
def
from
nonlocal
while
and
del
global
not
with
as
elif
if
or
yield
assert
else
import
pass
break
except
in
raise

# Não podemos usar palavras reservadas como nome de variável
break = 1
  Input In [25]
    break = 1
          ^
SyntaxError: invalid syntax


Variáveis Atribuídas a Outras Variáveis e Ordem dos Operadores

largura = 2

altura = 4

area = largura * altura

area
8

perimetro = 2 * largura + 2 * altura

perimetro
12

# A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2)  * altura

perimetro
32
Operações com Variáveis

idade1 = 25

idade2 = 35

idade1 + idade2
60

idade2 - idade1
10

idade2 * idade1
875

idade2 / idade1
1.4

idade2 % idade1
10
Concatenação de Variáveis

nome = "Bob"

sobrenome = "Marley"

fullName = nome + " " + sobrenome

fullName
'Bob Marley'
Fim
