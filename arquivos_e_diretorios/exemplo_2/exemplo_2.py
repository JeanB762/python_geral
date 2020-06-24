import os
import os.path
import shutil
from pathlib import Path


# Cria os arquivos
for el in range(10):
  Path(f'live_{el+1}.txt').touch()


# Encontra os arquivos com 'live_'
l = [f for f in os.listdir('.') if f.startswith('live_')]


# Remove os que o inteiro no nome forem menores ou iguais a 5
for _file in l:
  if int(_file.partition('_')[2][0]) <= 5:
    os.remove(_file)


# Renomeia os arquivos para live_n com n de 1 a 5
l_2 = [f for f in os.listdir('.') if f.startswith('live_')]
for val, el in enumerate(sorted(l_2)):
  shutil.move(el, 'live_{}'.format(val+1))

  
# Busca os arquivos e exibe
l_2 = [f for f in os.listdir('.') if f.startswith('live_')]
print(l_2)