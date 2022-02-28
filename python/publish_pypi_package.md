# Alpha-version of *Publishing a Package with PyPi

https://python-packaging.readthedocs.io/en/latest/minimal.html

## Requirements

install twine

need username on https://test.pypi.org/


## Lesson


Use the PyPI search to check if a name is already taken: https://pypi.org/search/



create gccalc folder:

mkdir gccalc

move gccalc.py to gccalc

mv gccalc.py gccalc

rename gccalc.py to __init__.py


in folder gccalc create setup.py

"""
from setuptools import setup

setup(name='GCcalculator',
      version='0.1',
      description='GC Calculator',
      url='https://github.com/Tillsa/GC_Calc',
      author='Till',
      author_email='sauerwein@zbmed.de',
      license='MIT',
      packages=['gccalc'],
      zip_safe=False)

"""

install locally

pip install .

open python

import gccalc

gccalc.calc_gc_content("GCAGCT")


pip list

pip uninstall GCcalculator



create a source distribution with:


$ python setup.py sdist bdist_wheel



$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*


# install twine
# need username on https://test.pypi.org/


$ pip install -i https://test.pypi.org/simple/ GCcalculator



open python

import gccalc

gccalc.calc_gc_content("GCAGCT")