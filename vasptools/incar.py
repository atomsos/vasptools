#!/usr/bin/env python3

import os
from io import StringIO
from configparser import ConfigParser
from . import utils
import re

incar_section_title = 'incar'
incar_section_string = '['+incar_section_title+']'
def parse_incar(incar=None):
    incar = incar or './INCAR'
    assert os.path.exists(incar), 'INCAR file should be given'
    buff = incar_section_string+'\n'
    with open(incar) as fd:
        buff += fd.read().lower()
    buff = re.sub('\n\s+', '\n', buff)
    conf = ConfigParser(inline_comment_prefixes=('#',';'))
    conf.read_string(buff)
    return conf._sections[incar_section_title]


def preview_parse_incar(incar=None):
    print(parse_incar(incar))



def output_incar(incar_dict=None):
    assert isinstance(incar_dict, dict), 'incar_dict should be a dict'
    incar_dict = {
        incar_section_title: incar_dict
        }
    conf = ConfigParser()
    conf.read_dict(incar_dict)
    buff = StringIO()
    conf.write(buff)
    buff = buff.getvalue()
    assert buff.startswith(incar_section_string), 'output_incar buff error: '+buff
    return buff[len(incar_section_string):]


def preview_output_incar(incar_dict=None):
    print(output_incar(incar_dict))


def gen_incar(incar_dict=None, dirname='.'):
    with open(os.path.join(dirname, 'INCAR')) as fd:
        fd.write(output_incar(incar_dict))




def test(TESTDIR='../test_dir'):
    assert isinstance(TESTDIR, str)
    if not os.path.isdir(TESTDIR):
        raise ValueError('You need to git clone the repo and run the test')
    incar = os.path.join(TESTDIR, 'INCAR_sample')
    incar_dict = parse_incar(incar)
    print(incar_dict)
    preview_output_incar(incar_dict)



if __name__ == '__main__':
    test()
