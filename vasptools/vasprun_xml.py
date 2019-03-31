"""
vasprun.xml parser
"""



import os
from . import format_parser


def find_vasprun_xml(filename='INCAR'):
    """
    find vasprun.xml with a filename
    """
    assert isinstance(filename, str) and filename.endswith('CAR'),\
        'filename should be a vasp file end with "CAR", however {0} is given.'.format(filename)
    vasprun_filename = os.path.join(os.path.dirname(filename), 'vasprun.xml')
    if not os.path.exists(vasprun_filename):
        raise IOError(vasprun_filename, 'not exists')
    return vasprun_filename


def vasprun_parser(vasprun_filename):
    """
    vasprun parser
    """
    return format_parser.read(vasprun_filename, format='vasp-xml')




def test(test_dir=None):
    """
    test vasprun
    """
    test_dir = test_dir or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test')
    assert isinstance(test_dir, str) and os.path.isdir(test_dir), \
        'test_dir: {0}\nYou need to git clone the repo and run the test'.format(test_dir)
    vasprun_filename = find_vasprun_xml(os.path.join(test_dir, 'INCAR'))
    print(vasprun_parser(vasprun_filename))
