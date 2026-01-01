#!/usr/bin/env python3
import tempfile
import shutil
from pathlib import Path
from playporter import main

tmp = Path(tempfile.mkdtemp())
try:
    src = tmp / "selenium_src"
    src.mkdir()
    dest = tmp / "playwright_dest" / "converted"
    rc = main.main(["--migrate", str(src), str(dest)])
    print("RC:", rc)
finally:
    shutil.rmtree(tmp)
