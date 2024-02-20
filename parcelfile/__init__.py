import sys
import os
from zipfile import ZipFile
from . import P_Requirments as pr #personal module for unnamed functions


class colors:
  red = '\033[91m'
  green = '\033[92m'
  yellow = '\033[93m'
  blue = '\033[94m'
  magenta = '\033[95m'
  cyan = '\033[96m'
  white = '\033[97m'
  end = '\033[0m'

#=====literals=====
ZIPPED = pr.mode['zipped']
STR = pr.type['str']
INT = pr.type['int']
BOOL = pr.type['bool']
FLOAT = pr.type["float"]
MULTI = pr.type['other']

__all__ = (
  ZIPPED,
  STR,
  INT,
  BOOL,
  FLOAT,
  MULTI,
  __builtins__,
  __name__,
)