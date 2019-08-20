# CREADO POR VINICIO VALBUENA
# NO ESTA ORGANIZADO SOLO ES PARA EXPLICAR EL
# FUNCIONAMIENTO

import re

DATA = None
DUMMY_DATA = { # YO DEBERIA SER UN ARCHIVO APARTE
    'NAME': 'VINICIO',
    'LIKE': 'PROGRAMAR',
} # IGNORADO PERO CON TEMPLATE PARA CREARLO

# leemos el archivo y lo carga de manera temporal
# la mejor forma de manejar esto de forma dinamica es
# utilizando una class que gestione este proceso ya que
# asi DATA no seria compartida
with open('info.txt', 'r') as f:
    DATA = f.read()

# expreg para filtrar
p = re.compile(r'{{(.*)}}')
keys = p.findall(DATA)

# map variable
for key in keys:
    _p = re.compile('{{{KEY}}}'.format(**{
        'KEY': key,
    }))
    DATA = re.sub(_p, DUMMY_DATA.get(key), DATA)

print(DATA)
