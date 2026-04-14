import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent
sys.path.append(str(ROOT_DIR))

from tools import json_output
print(json_output("今天天气真好"))