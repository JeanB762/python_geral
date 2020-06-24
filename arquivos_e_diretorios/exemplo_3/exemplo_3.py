import os
import os.path
import shutil
from pathlib import Path


# Criação sequencial das pastas
for x in range(1, 11):
  dir_ = 'pasta_{}'.format(x)
  if not os.path.exists(dir_):
    os.mkdir(dir_)


# Listagem das pastas
l = [path for path in os.listdir('.') if os.path.isdir(path)]

# Criação dos arquivos nas respéctivas pastas
for path in l:
  Path(os.path.join(path, 'arquivo_1.txt')).touch()
  Path(os.path.join(path, 'arquivo_2.txt')).touch()
  # Path('{}/arquivo_1.txt'.format(path)).touch()
  # Path('{}/arquivo_2.txt'.format(path)).touch()


for val in os.walk('.'):
  print(val)