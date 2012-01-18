'''
>>> trunca("Joaquim loca Silva",100)
('Joaquim loca Silva', '')
>>> trunca("Joaquim loca Silva",10)
('Joaquim ', 'loca Silva')
>>> trunca("loca Silva",10)
('loca Silva', '')
>>> corta_tudo("Joaquim loca Silva", 10)
['Joaquim ', 'loca Silva']
>>> ver_truncado("Joaquim loca Silva", 10) == res_final
True
'''
from quebra_linha import trunca, corta_tudo, ver_truncado

res_final = '''Joaquim \nloca Silva'''


if __name__ == '__main__':
    import doctest
    doctest.testmod()