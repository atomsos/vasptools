"""
utils used by vasptools
"""
import os
import platform
from io import StringIO
import sh






POSSIBLE_POTCAR_ENV = ['VASPPOT', 'VASP_PP_PATH', 'VASPPOT_HOME',]
VALID_PP_TYPES = ['potcar', 'potcarGGA', 'potpaw', 'potpaw_GGA', 'potpaw_PBE']
CHEMICAL_SYMBOLS = ['X', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F',
                    'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',
                    'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
                    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh',
                    'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
                    'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu',
                    'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
                    'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',
                    'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es',
                    'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs',
                    'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts',
                    'Og']


global VASPPOT_PATH
VASPPOT_PATH = None



def reset_vasppot_path():
    global VASPPOT_PATH
    for env in POSSIBLE_POTCAR_ENV:
        if env in os.environ:
            VASPPOT_PATH = os.environ[env]
            break

reset_vasppot_path()



