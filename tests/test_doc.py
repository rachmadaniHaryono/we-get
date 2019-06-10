from datetime import datetime


def test_arg_option_doc():
    with open('README.rst') as f:
        content = f.read()
    option_parts = content.split('Options\n-------')[1].split('Video options\n')[0].strip()
    option_parts = option_parts.splitlines()[1:-1]
    option_parts = [x.split(' ', 2) for x in option_parts]
    for idx, x in enumerate(option_parts):
        option_parts[idx][2] = x[2].strip()
    with open('we_get/core/we_get.py') as f:
        m_content = f.read()
    m_option_parts = m_content.split('Options:')[1].split('Video options')[0].strip().splitlines()
    m_option_parts = [x.strip().split(' ', 2) for x in m_option_parts]
    for idx, x in enumerate(m_option_parts):
        m_option_parts[idx][2] = x[2].strip()
    assert option_parts == m_option_parts


def test_year():
    current_year = datetime.now().year
    with open('we_get/core/we_get.py') as f:
        m_content = f.read()
    m_content.splitlines()[1]
    year = m_content.split('Copyright (c) 2016-')[1].split(' ')[0]
    assert year == str(current_year)
