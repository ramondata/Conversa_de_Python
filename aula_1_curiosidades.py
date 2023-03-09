# Aula 1: Curiosidades da linguagem Python

# O nome Python é derivado da série de tv Monty Python`s flying circus disponivel na netflix,
# e o fundador da linguagem, cuja série favorita era esta é o Guido Van Rossum.

# Linguagem interpretada, ou seja, não necessita de um compilador e nem gerar um bytecode

# Possui variantes para linguagem C e Java, CPython e Jython respectivamente

# else em estrutura de repetição for

# Funções podem retornar uma estrutura de dados com vários dados ao invés de apenas 1 dado

import this


numero = 123_456_789
print(numero)

var_1: int = 1
_id_1 = id(var_1)
var_2: int = 1
_id_2 = id(var_2)
_is = _id_1 is _id_2
_in = _id_1 in [_id_2]
print(_is)
print(_in)

recebe_varias_entradas = 1,2,3
a, b, c = recebe_varias_entradas

import calendar
calendar.month(year, month, day)

import psutils
#add alguma demonstração

#add demostraçao de writexlsx e openpyxl

# demonstração com pyautogui
