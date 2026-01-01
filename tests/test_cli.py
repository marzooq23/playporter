import os
from pathlib import Path

import pytest

from playporter import main as cli


def test_migrate_arg_parsing_and_missing_tool(tmp_path: Path):
    # create a fake source directory
    src = tmp_path / "selenium_src"
    src.mkdir()

    # destination path (nested) - does not need to exist beforehand
    dest = tmp_path / "playwright_dest" / "converted"

    # run the CLI with the --migrate args
    result = cli.main(["--migrate", str(src), str(dest)])

    # since no migration implementation exists by default, migrate_framework returns 1
    assert result == 1


def test_migrate_with_language_and_short_flag(tmp_path: Path):
    src = tmp_path / "selenium_src_lang"
    src.mkdir()
    dest = tmp_path / "playwright_dest_lang" / "converted"

    # long form with language
    result_long = cli.main(["--migrate", str(src), str(dest), "typescript"])
    assert result_long == 1

    # short form with language
    result_short = cli.main(["-m", str(src), str(dest), "python"])
    assert result_short == 1
