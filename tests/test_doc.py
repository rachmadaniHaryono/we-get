from datetime import datetime
from pathlib import Path

import pytest


def test_arg_option_doc():
    readme_path = Path(__file__).parent.parent / "README.rst"
    with readme_path.open() as f:
        content = f.read()
    option_parts = (
        content.split("Options\n-------")[1].split("Video options\n")[0].strip()
    )
    option_parts = option_parts.splitlines()[1:-1]
    option_parts = [x.split(" ", 2) for x in option_parts]
    for idx, x in enumerate(option_parts):
        option_parts[idx][2] = x[2].strip()
    we_get_path = Path(__file__).parent.parent / "we_get" / "core" / "we_get.py"
    with we_get_path.open() as f:
        m_content = f.read()
    m_option_parts = (
        m_content.split("Options:")[1].split("Video options")[0].strip().splitlines()
    )
    m_option_parts = [x.strip().split(" ", 2) for x in m_option_parts]
    for idx, x in enumerate(m_option_parts):
        m_option_parts[idx][2] = x[2].strip()
    assert option_parts == m_option_parts


@pytest.mark.parametrize(
    "path",
    [
        Path(__file__).parent.parent / "we_get" / "__init__.py",
        Path(__file__).parent.parent / "we_get" / "core" / "__init__.py",
        Path(__file__).parent.parent / "we_get" / "core" / "commands.py",
        Path(__file__).parent.parent / "we_get" / "core" / "completer.py",
        Path(__file__).parent.parent / "we_get" / "core" / "module.py",
        Path(__file__).parent.parent / "we_get" / "core" / "shell.py",
        Path(__file__).parent.parent / "we_get" / "core" / "style.py",
        Path(__file__).parent.parent / "we_get" / "core" / "utils.py",
        Path(__file__).parent.parent / "we_get" / "core" / "we_get.py",
        Path(__file__).parent.parent / "we_get" / "modules" / "1337x.py",
        Path(__file__).parent.parent / "we_get" / "modules" / "__init__.py",
        Path(__file__).parent.parent / "we_get" / "modules" / "eztv.py",
        Path(__file__).parent.parent / "we_get" / "modules" / "the_pirate_bay.py",
        Path(__file__).parent.parent / "we_get" / "modules" / "yts.py",
        Path(__file__).parent.parent / "setup.py",
    ],
)
def test_year(path):
    current_year = datetime.now().year
    with path.open() as f:
        m_content = f.read()
    m_content.splitlines()[1]
    year = m_content.split("Copyright (c) 2016-")[1].split(" ")[0]
    assert year == str(current_year)


def test_version():
    setup_path = Path(__file__).parent.parent / "setup.py"
    with setup_path.open() as f:
        v_line = next(
            filter(lambda x: x.startswith("version = "), f.read().splitlines())
        )
    from we_get.core.we_get import __version__

    assert '"{}"'.format(__version__) == v_line.split("=")[1].strip()
