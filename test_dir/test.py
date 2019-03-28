#!/usr/bin/env python3



import os
BASEDIR = os.path.dirname(os.path.abspath(__file__))
os.environ['VASPPOT'] = os.path.join(BASEDIR, 'vasppot_sample')
print(os.environ['VASPPOT'])



import vasptools
def test():
    error_mod = []
    exitcode = 0
    for mod in vasptools.__all_modules__:
        if hasattr(mod, 'test'):
            print(mod.__name__)
            try:
                mod.test(BASEDIR)
            except:
                error_mod.append(mod)
                exitcode = 1
    if exitcode == 0:
        print('ALL SUCCEESS')
    else:
        print('ERROR MODS:', ','.join([mod.__name__ for mod in error_mod]))
    exit(exitcode)

if __name__ == '__main__':
    test()
