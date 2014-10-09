import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)
# this sets __version__
info = {}
execfile(os.path.join('data_services_library', 'version.py'), info)


with open('README.rst') as f:
    # use README for long description but don't include the link to travis-ci;
    # it seems a bit out of place on pypi since it applies to the development
    # version
    long_description = ''.join([
        line for line in f.readlines()
        if 'travis-ci' not in line])


setup(
    name='data_services_library',
    version=info['__version__'],
    license='',
    author='Dharhas Pothina',
    author_email='dharhas.pothina@erdc.dren.mil',
    description='Environmental Simulator, Data Services, Interpolation, Web Services',
    long_description=long_description,
    url='',
    keywords='',
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'appdirs>=1.2.0',
        'numpy>=1.4.0',
        'stevedore',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: :: ',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],


    include_package_data=True,

    entry_points={
        'data_services_library.services': [
            'usgs-nwis-iv = data_services_library.services.usgs_nwis:UsgsNwisIV',
            'usgs-nwis-dv = data_services_library.services.usgs_nwis:UsgsNwisDV',
            'ncdc-ghcn = data_services_library.services.ncdc_ghcn:NcdcGhcn',
            'ncdc-gsod = data_services_library.services.ncdc_gsod:NcdcGsod',
            'example-points = data_services_library.services.example:ExamplePoints',
            'example-polys = data_services_library.services.example:ExamplePolys'
        ],
    },

    zip_safe=False,

    tests_require=[
        'pytest>=2.3.2',
    ],
    cmdclass={'test': PyTest},
)