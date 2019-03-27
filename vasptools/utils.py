import os
import sh
import platform
from io import StringIO




BASEDIR = os.path.dirname(os.path.abspath(__file__))
TESTDIR = os.path.join(BASEDIR, '..', 'test_dir')

possible_potcar_env = ['VASP_PP_PATH', 'VASPPOT', 'VASPPOT_HOME',]
valid_pp_types = ['potcar', 'potcarGGA', 'potpaw', 'potpaw_GGA', 'potpaw_PBE']


vasppot_path = None
for env in possible_potcar_env:
    if env in os.environ:
        vasppot_path = os.environ[env]
        break



def get_file_content(filename):
    assert os.path.exists(filename), filename+' not exists'
    _, extension = os.path.splitext(filename)
    if extension == '':
        with open(filename) as fd:
            output = fd.read()
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
            args    = config_table['args']
            args.append(filename)
            args = tuple(args)
            sh.Command(command).__call__(*args, _out=buff)
        elif platform.system() in ['Windows']:
            raise NotImplementedError('.Z not support windows for now')
        else:
            raise NotImplementedError('Unknown system')
        return buff.getvalue()
