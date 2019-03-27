#!/usr/bin/env python3




import vasptools




def test():
    for mod in vasptools.__all_modules__:
        if hasattr(mod, 'test'):
            print(mod.__name__)
            mod.test()

if __name__ == '__main__':
    test()
