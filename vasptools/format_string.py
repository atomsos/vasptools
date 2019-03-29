"""
format_string contain vasp-out
"""
from .format_parser import ExtList, datablock_to_numpy


FORMAT_STRING = {
    'vasp-out': {
        'calculator' : 'VASP',
        'ignorance' : None,
        'primitive_data': {
            r'free  energy   TOTEN\s*=\s*(.*?)\s+eV\s*\n' : {
                'important' : True,
                'selection' : -1,
                'type' : float,
                'key' : 'calc_arrays/freeE',
                },
            r'energy  without entropy=\s*(.*?)\s+' : {
                'important' : True,
                'selection' : -1,
                'type' : float,
                'key' : 'calc_arrays/E_without_S',
                },
            r'energy\(sigma->0\)\s*=\s*(.*)' : {
                'important' : True,
                'selection' : -1,
                'type' : float,
                'key' : 'calc_arrays/potential_energy',
                },
            r'ions per type\s*=\s*(.*)\n' : {
                'important' : True,
                'selection' : -1,
                'type' : list,
                'process' : lambda x: datablock_to_numpy(x).astype(int).flatten(),
                'key' : 'ions_per_type',
                },
            r'VRHFIN\s*=\s*(.*?):' : {
                'important' : True,
                'selection' : 'all',
                'type' : ExtList,
                'key' : 'elements_per_type',
                },
            r'POSITION\s*TOTAL-FORCE[\s\S]*?-{2,}\n([\s\S]*?)\n\s+-{2,}' : {
                'important' : True,
                'selection' : -1,
                'process' : datablock_to_numpy,
                'key' : [
                    {
                        'key' : 'positions',
                        'type': float,
                        'index': ':,:3'
                    },
                    {
                        'key' : 'calc_arrays/forces',
                        'type': float,
                        'index': ':,3:6'
                    },
                    ],
                },
            r'FORCES acting on ions[\s\S]*?-{2,}\n([\s\S]*?)\s+-{2,}': {
                'important' : True,
                'selection' : -1,
                'process' : datablock_to_numpy,
                'key': [
                    {
                        'key' : 'calc_arrays/forces_e_ion',
                        'type': float,
                        'index' : ':,0:3'
                    },
                    {
                        'key' : 'calc_arrays/forces_ewald',
                        'type': float,
                        'index' : ':,3:6'
                    },
                    {
                        'key' : 'calc_arrays/forces_nonlocal',
                        'type': float,
                        'index' : ':,6:9'
                    },
                    {
                        'key' : 'calc_arrays/forces_convergence_correction',
                        'type': float,
                        'index' : ':,9:12'
                    },
                    ],
                },
            },
        'synthesized_data' : {
            'symbols' : {
                'equation' : lambda arrays: arrays['elements_per_type'] * arrays['ions_per_type'],
                },
        },
    },
}
