"""



VASP Input/Output



"""




import chemio




def read(filename, filetype=None):
    return chemio.read(filename, filetype)


def write(filename, arrays, filetype=None):
    chemio.write(filename, arrays, filetype)


def preview(arrays, filetype):
    chemio.preview(arrays, filetype)

