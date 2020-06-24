import os
import os.path
import shutil
from pathlib import Path


# Criação sequencial das pastas
for x in range(1, 11):
  os.mkdir('pasta_{}'.format(x))


# Listagem das pastas
l = [path for path in os.listdir('.') if os.path.isdir(path)]

# Criação dos arquivos nas respéctivas pastas
for path in l:
  Path('{}/arquivo_1.txt'.format(path)).touch()
  Path('{}/arquivo_2.txt'.format(path)).touch()