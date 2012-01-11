#!/usr/bin/env python
#coding: utf-8
"""
>>> verifica_divisivel(3, 3)
True
>>> verifica_divisivel(4, 3)
False
>>> verifica_divisivel(5, 5)
True
>>> verifica_divisivel(4, 5)
False
>>> verifica_numero(2)
2
>>> verifica_numero(3)
'Fizz'
>>> verifica_numero(4)
4
>>> verifica_numero(5)
'Buzz'
>>> verifica_numero(90)
'FizzBuzz'
>>> 'BuzzFizz' in [verifica_numero(i) for i in range(1, 101)]
False
>>> lista_auto = [verifica_numero(i) for i in range(1, 11)]
>>> lista_auto == [1, 2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
True
>>>
"""

from fizzbuzz import verifica_divisivel
from fizzbuzz import verifica_numero

if __name__ == '__main__':
    import doctest
    doctest.testmod()