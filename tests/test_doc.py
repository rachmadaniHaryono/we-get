from datetime import datetime
from pathlib import Path


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


def test_year():
    current_year = datetime.now().year
    path = Path(__file__).parent.parent / "we_get" / "core" / "we_get.py"
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
