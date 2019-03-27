#!/usr/bin/env python3


import os, glob
import utils

def get_potcar_content(pp_names=None, pp_type='potpaw_PBE'):
    assert utils.vasppot_path is not None, \
        'To use get_potcar, you need set VASPPOT env'
    assert isinstance(pp_names, list) or isinstance(pp_names, tuple), \
        'You need to give a list or tuple as pp_names'
    assert len(pp_names) > 0, 'pp_names needs content'
    assert pp_type in utils.valid_pp_types

    output = ''
    for name in pp_names:
        path = os.path.join(utils.vasppot_path, pp_type, name, 'POTCAR*')
        candidate = glob.glob(path)
        if len(candidate) == 0:
            raise ValueError(pp_type+' may not have '+name)
        elif len(candidate) > 1:
            raise Warning(name+' in '+pp_type+' has more than 1 candiate')
        output += utils.get_file_content(candidate[0])
    return output


def gen_potcar(pp_names=None, pp_type='potpaw_PBE'):
    with open('POTCAR', 'w') as fd:
        fd.write(get_potcar_content(pp_names, pp_type))



