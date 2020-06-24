import os
import os.path
import shutil
from pathlib import Path


# Criar path caso ele não exista
if not os.path.exists('aulinha_1'):
   os.mkdir('aulinha_1')

# Criar arquivo xpto
Path('aulinha_1/xpto.txt').touch()