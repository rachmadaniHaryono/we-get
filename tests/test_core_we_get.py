import pytest
from docopt import docopt, DocoptExit

from we_get.core.we_get import WG
from we_get.core import we_get


@pytest.mark.parametrize(
    'argv, exp_res',
    [
        [None, {'arguments': None, 'parguments': {}, 'we_get_run': 0}],
        [['--search', 'ubuntu'],  {
            'arguments': {
                '--filter': [],
                '--genre': [],
                '--get-list': 0,
                '--help': 0,
                '--ignore-http-error': 0,
                '--json': 0,
                '--links': 0,
                '--list': 0,
                '--quality': [],
                '--results': [],
                '--search': ['ubuntu'],
                '--sort-type': [],
                '--target': ['all'],
                '--version': 0
            },
            'parguments': {
                '--search': ['ubuntu'], '--target': ['all']}, 'we_get_run': 1
        }],
    ]
)
def test_parse_arguments(argv, exp_res):
    wg = WG()
    if argv is None:
        with pytest.raises(DocoptExit):
            wg.parse_arguments()
        assert vars(wg) == exp_res
        with pytest.raises(DocoptExit):
            wg.parse_arguments(argv)
        assert vars(wg) == exp_res
    else:
        wg.parse_arguments(argv)
        assert vars(wg) == exp_res


@pytest.mark.parametrize(
    'argv, exp_res',
    [
        [
            [],
            {
                '--filter': [], '--genre': [], '--get-list': 0, '--help': 0,
                '--ignore-http-error': 0, '--json': 0, '--links': 0, '--list': 0, '--quality': [],
                '--results': [], '--search': [], '--sort-type': [], '--target': ['all'],
                '--version': 0}
        ],
    ],
)
def test_we_get_docopt(argv, exp_res):
    res = docopt(we_get.__doc__, argv=argv)
    assert exp_res == res
