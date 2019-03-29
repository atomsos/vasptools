"""
vasptools __init__
"""



from . import api
from . import potcar
from . import poscar
from . import incar
from . import kpoints
from . import doscar
from . import outcar
from . import wavecar
from . import chgcar
from . import chg

__all_modules__ = [
    potcar,
    poscar,
    incar,
    kpoints,
    doscar,
    outcar,
    wavecar,
    chgcar,
    chg,
    ]



__version__ = '0.3.2'
def version():
    return __version__
