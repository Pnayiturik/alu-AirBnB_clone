#!/usr/bin/python3
from models.engine.file_storage import FileStorage

import sys
sys.path.append('..')

storage = FileStorage()
storage.reload()
