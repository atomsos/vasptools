"""
This module resolve VASP POTCAR related.
"""

import os
import glob
from . import utils

POTCAR_STRING = 'POTCAR'


def get_potcar_content(pp_names=None, pp_type='potpaw_PBE'):
    """
    Using VASPPOT_PATH to combine a POTCAR string with pp_names
    """
    assert utils.VASPPOT_PATH is not None, \
        'To use get_potcar, you need set VASPPOT env'
    assert isinstance(pp_names, (list, tuple)), \
        'You need to give a list or tuple as pp_names'
    assert pp_names, 'pp_names needs content'
    assert pp_type in utils.VALID_PP_TYPES, '{0} should belongs {1}'.format(pp_type, utils.VALID_PP_TYPES)

    output = ''
    for name in pp_names:
        path = os.path.join(utils.VASPPOT_PATH, pp_type, name, POTCAR_STRING+'*')
        candidate = glob.glob(path)
        if not candidate:
            raise ValueError(pp_type+' may not have '+name)
        elif len(candidate) > 1:
            raise Warning(name+' in '+pp_type+' has more than 1 candiate')
        output += utils.get_file_content(candidate[0])
    return output


def gen_potcar(pp_names=None, pp_type='potpaw_PBE', dirname='.'):
    """
    Generate a POTCAR directly
    """
    assert isinstance(dirname, str) and os.path.isdir(dirname), \
        'dirname should exist'
    filename = os.path.join(dirname, POTCAR_STRING)
    with open(filename, 'w') as _fd:
        _fd.write(get_potcar_content(pp_names, pp_type))


def test(test_dir=None):
    """
    test of potcar
    """
    test_dir = test_dir or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test_dir')
    os.environ['VASPPOT'] = os.path.join(test_dir, 'vasppot_sample')
    print(get_potcar_content(['H', 'He', 'Li'])[:1000])
    gen_potcar(['H', 'He', 'Li'], dirname='/tmp')
