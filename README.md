# vasptools
tools for vasp

[![Build Status](https://travis-ci.org/atomse/vasptools.svg?branch=master)](https://travis-ci.org/atomse/vasptools)


## Installation
```python
pip install vasptools
```


## POSCAR
```python
>>> from vasptools import potcar
>>> potcar.get_potcar_content(pp_names=['H', 'He', 'Li', pp_type='potpaw_PBE')
' PAW_PBE H 15Jun2001\n 1.00000000000000000\n parameters from PSCTR are:\n   VRHFIN =H: ultrasoft test\n '
>>> potcar.gen_potcar(pp_names=['H'], pp_type='potpaw_PBE')

```

## INCAR
```python
>>> from vasptools import incar
>>> incar_dict = incar.parse_incar(incarfile)
>>> print(incar_dict)
OrderedDict([('system', 'si series'), ('prec', 'accurate'), ('encut', '245.345'), ('ibrion', '-1'), ('nsw', '0'), ('nelmin', '2'), ('ediff', '1.0e-05'), ('ediffg', '-0.02'), ('voskown', '1'), ('nblock', '1'), ('lvtot', '.true.'), ('nelm', '60'), ('algo', 'fast   (blocked davidson)'), ('gga', 'pe'), ('ispin', '1'), ('iniwav', '1'), ('istart', '0'), ('icharg', '2'), ('lwave', '.false.'), ('lcharg', '.true.'), ('addgrid', '.false.'), ('lhyperfine', '.false.'), ('ismear', '0'), ('sigma', '0.2'), ('rwigs', '1.11')])
>>> print(output_incar(incar_dict))
system = si series
prec = accurate
encut = 245.345
ibrion = -1
nsw = 0
nelmin = 2
```



## TODO
- [x] INCAR
- [ ] POSCAR
- [ ] KPOINTS
- [ ] OUTCAR
- [ ] DOSCAR
- [ ] CHGCAR
- [ ] CHG
- [ ] WAVECAR

...

