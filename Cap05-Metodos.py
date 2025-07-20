Métodos
Tudo em Python é objeto. E cada objeto tem métodos e atributos.
Atributos são propriedades, características do objeto.
Métodos são funções com ações que podem ser executadas nos objetos.

# Criando uma lista
lista = [100, -2, 12, 65, 0]

type(lista)
list

# Verificando métodos e atributos
lista
[100, -2, 12, 65, 0]

# Usando um método do objeto lista
lista.append(100)

# Imprimindo a lista
print(lista)
[100, -2, 12, 65, 0, 100]

# Usando um método do objeto lista
lista.count(100)
2

# A função help() explica como utilizar cada método de um objeto
help(lista.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.


# A função dir() mostra todos os métodos e atributos de um objeto
dir(lista)
['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']

frase = 'Isso é uma string'

type(frase)
str

# Verificando métodos e atributos
frase
'Isso é uma string'

# O método de um objeto pode ser chamado dentro de uma função, como print()
print (frase.split())
['Isso', 'é', 'uma', 'string']
Fim¶
