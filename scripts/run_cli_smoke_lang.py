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
    rc1 = main.main(["--migrate", str(src), str(dest), "typescript"])
    print("RC1:", rc1)
    rc2 = main.main(["-m", str(src), str(dest), "python"])
    print("RC2:", rc2)
finally:
    shutil.rmtree(tmp)
