import os
import os.path
import shutil
from pathlib import Path

for x in range(1, 11):
  os.mkdir('pasta_{}'.format(x))

l = [path for path in os.listdir('.') if os.path.isdir(path)]

print(l)