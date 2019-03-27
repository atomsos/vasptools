# vasptools
tools for vasp

[![Build Status](https://travis-ci.org/atomse/vasptools.svg?branch=master)](https://travis-ci.org/atomse/vasptools)


## POSCAR
```python
>>> from vasptools import potcar
>>> potcar.get_potcar_content(pp_names=['H', 'He', 'Li', pp_type='potpaw_PBE')
' PAW_PBE H 15Jun2001\n 1.00000000000000000\n parameters from PSCTR are:\n   VRHFIN =H: ultrasoft test\n '
>>> potcar.gen_potcar(pp_names=['H'], pp_type='potpaw_PBE')

```



## TODO
- [ ] INCAR
- [ ] POSCAR
- [ ] KPOINTS
- [ ] OUTCAR
- [ ] DOSCAR
- [ ] CHGCAR
- [ ] CHG
- [ ] WAVECAR

...

