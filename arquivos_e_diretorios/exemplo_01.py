import os
import os.path
import shutil
from pathlib import Path


# Criar path caso ele não exista
if not os.path.exists('aulinha_1'):
   os.mkdir('aulinha_1')

os.chdir('aulinha_1')

# Criar arquivo xpto
Path('xpto.txt').touch()

shutil.copy('xpto.txt', 'xpto_1.txt')
shutil.copy('xpto.txt', 'xpto_2.txt')
shutil.copy('xpto.txt', 'xpto_3.txt')