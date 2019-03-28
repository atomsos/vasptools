"""
utils used by vasptools
"""
import os
import platform
from io import StringIO
import sh






POSSIBLE_POTCAR_ENV = ['VASP_PP_PATH', 'VASPPOT', 'VASPPOT_HOME',]
VALID_PP_TYPES = ['potcar', 'potcarGGA', 'potpaw', 'potpaw_GGA', 'potpaw_PBE']


VASPPOT_PATH = None
for env in POSSIBLE_POTCAR_ENV:
    if env in os.environ:
        VASPPOT_PATH = os.environ[env]
        break



def get_file_content(filename):
    """
    Get file content, for plain text, .xz, .Z, .gz
    """
    assert os.path.exists(filename), filename+' not exists'
    _, extension = os.path.splitext(filename)
    if extension == '':
        with open(filename) as _fd:
            output = _fd.read()
        return output
    else:
        linux_darwin_config_table = {
            '.Z': {
                'command': 'uncompress',
                'args': ['-c',],
            },
            '.xz': {
                'command': 'xz',
                'args': ['-c', '-d'],
            },
            '.gz': {
                'command': 'gzip',
                'args': ['-c', '-d'],
            },
        }
        buff = StringIO()
        if platform.system() in ['Darwin', 'Linux']:
            config_table = linux_darwin_config_table
            assert extension in config_table, extension+' has not config'
            config_table = config_table[extension]
            command = config_table['command']
            args = config_table['args']
            args.append(filename)
            args = tuple(args)
            sh.Command(command)(*args, _out=buff)
        elif platform.system() in ['Windows']:
            raise NotImplementedError('.Z not support windows for now')
        else:
            raise NotImplementedError('Unknown system')
        return buff.getvalue()
