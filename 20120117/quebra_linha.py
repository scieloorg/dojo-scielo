"""
http://dojopuzzles.com/problemas/exibe/quebra-de-linha/
"""


def trunca(texto, col):

    if col >= len(texto):
        return (texto,'')

    r = texto[:col] #Joaquim lo
    r2 = texto[col:] #ca Silva
    #False or False
    if r.endswith(' ') or r2.startswith(' '):
        #res = 'Joaquim lo'
        res = r
        #resto = ca Silva
        resto = r2
    else:
        #res = 7
        res = r[:r.rfind(' ')+1]
        #resto =
        resto = texto[len(res):]

    return (res, resto)

def corta_tudo(tudo, col):
    resto = tudo
    l = []
    while resto != '':
        v, resto = trunca(resto, col)
        l.append(v)
    return l

def ver_truncado(texto, col):
    trechos = corta_tudo(texto, col)
    return '\n'.join(trechos)


