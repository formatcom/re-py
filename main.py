# CREADO POR VINICIO VALBUENA
# NO ESTA ORGANIZADO SOLO ES PARA EXPLICAR EL
# FUNCIONAMIENTO

import re

DATA = None
DUMMY_DATA = __import__('setting')

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
    _p = re.compile('{{%s}}' % key)
    DATA = re.sub(_p, getattr(DUMMY_DATA, key, 'Undefined'), DATA)

print(DATA)
