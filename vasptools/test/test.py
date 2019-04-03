#!/usr/bin/env python3



import os
import argparse

BASEDIR = os.path.dirname(os.path.abspath(__file__))
os.environ['VASPPOT'] = os.path.join(BASEDIR, 'vasppot_sample')



import vasptools

def test(args):
    error_mod = []
    exitcode = 0
    for mod in vasptools.__test_modules__:
        if hasattr(mod, 'test'):
            if args.mod and not mod.__name__.split('.')[-1] in args.mod:
                continue
            print(mod.__name__)
            try:
                mod.test(BASEDIR)
            except Exception as e:
                print(e)
                error_mod.append(mod)
                exitcode = 1
    if exitcode == 0:
        print('ALL SUCCEESS')
    else:
        print('ERROR MODS:', ','.join([mod.__name__ for mod in error_mod]))
    exit(exitcode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("mod", nargs='*')
    args = parser.parse_args()

    test(args)
