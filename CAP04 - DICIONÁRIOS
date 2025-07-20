Trabalhando com Dicionários

# Isso é uma lista
estudantes_lst = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]   

estudantes_lst
['Pedro', 24, 'Ana', 22, 'Ronaldo', 26, 'Janaina', 25]

type(estudantes_lst)
list

# Isso é um dicionário
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}

estudantes_dict 
{'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Janaina': 25}

type(estudantes_dict)
dict

estudantes_dict["Pedro"]
24

estudantes_dict["Marcelo"] = 23

estudantes_dict["Marcelo"]
23

estudantes_dict 
{'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Janaina': 25, 'Marcelo': 23}

estudantes_dict.clear()

estudantes_dict
{}

del estudantes_dict

estudantes_dict
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/var/folders/dc/lqrc3k5j4438r150cbrdr_000000gn/T/ipykernel_3029/1634695477.py in <module>
----> 1 estudantes_dict

NameError: name 'estudantes_dict' is not defined


estudantes = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}

estudantes
{'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Janaina': 25}

len(estudantes)
4

estudantes.keys()
dict_keys(['Pedro', 'Ana', 'Ronaldo', 'Janaina'])

estudantes.values()
dict_values([24, 22, 26, 25])

estudantes.items()
dict_items([('Pedro', 24), ('Ana', 22), ('Ronaldo', 26), ('Janaina', 25)])

estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}

estudantes2
{'Camila': 27, 'Adriana': 28, 'Roberta': 26}

estudantes.update(estudantes2)

estudantes
{'Pedro': 24,
 'Ana': 22,
 'Ronaldo': 26,
 'Janaina': 25,
 'Camila': 27,
 'Adriana': 28,
 'Roberta': 26}

dic1 = {}

dic1
{}

dic1["chave_um"] = 2

print(dic1)
{'chave_um': 2}

dic1[10] = 5

dic1
{'chave_um': 2, 10: 5}

dic1[9.13] = "Python"

dic1
{'chave_um': 2, 10: 5, 9.13: 'Python'}

dic1["teste"] = 5

dic1
{'chave_um': 2, 10: 5, 9.13: 'Python', 'teste': 5}

dict1 = {}

dict1
{}

dict1["teste"] = 10

dict1["key"] = "teste"

# Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.
dict1
{'teste': 10, 'key': 'teste'}

dict2 = {}

dict2["key1"] = "Data Science"

dict2["key2"] = 10

dict2["key3"] = 100

dict2
{'key1': 'Data Science', 'key2': 10, 'key3': 100}

a = dict2["key1"]

b = dict2["key2"]

c = dict2["key3"]

a, b, c
('Data Science', 10, 100)

# Dicionário de listas
dict3 = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}

dict3
{'chave1': 1230,
 'chave2': [22, 453, 73.4],
 'chave3': ['picanha', 'fraldinha', 'alcatra']}

dict3['chave2']
[22, 453, 73.4]

# Acessando um item da lista, dentro do dicionário
dict3['chave3'][0].upper()
'PICANHA'

# Operações com itens da lista, dentro do dicionário
var1 = dict3['chave2'][0] - 2

var1
20

# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['chave2'][0] -= 2

dict3
{'chave1': 1230,
 'chave2': [20, 453, 73.4],
 'chave3': ['picanha', 'fraldinha', 'alcatra']}
Criando Dicionários Aninhados

# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}

dict_aninhado
{'key1': {'key2_aninhada': {'key3_aninhada': 'Dict aninhado em Python'}}}

dict_aninhado['key1']['key2_aninhada']['key3_aninhada']
'Dict aninhado em Python'
Fim
