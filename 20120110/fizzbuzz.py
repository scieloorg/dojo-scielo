#!/usr/bin/env python
#coding: utf-8
"""
Problema: FizzBuzz
http://dojopuzzles.com/problemas/exibe/fizzbuzz/


Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

 - Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
 - Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
 - Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""

def verifica_divisivel(x, y):
    return True if x % y == 0 else False

def verifica_numero(num):
    retorno = ''
    if verifica_divisivel(num, 3):
        retorno +='Fizz'
    if verifica_divisivel(num, 5):
        retorno +='Buzz'

    if len(retorno) == 0:
        return num
    else:
        return retorno

if __name__ == '__main__':

    for i in range(1,101):
        print verifica_numero(i)

