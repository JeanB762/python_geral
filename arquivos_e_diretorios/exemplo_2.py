import os
import os.path
import shutil
from pathlib import Path


for el in range(10):
  Path(f'live_{el}.txt').touch()


l = [f for f in os.listdir('.') if f.startswith('live_')]

for _file in l:
  if int(_file.partition('_')[2][0]) <= 5:
    os.remove(_file)