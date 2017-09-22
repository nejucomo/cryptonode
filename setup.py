#!/usr/bin/env python

from setuptools import setup, find_packages


PACKAGE = 'cryptonode'

setup(
    name=PACKAGE,
    description='Manager multiple cryptocurrency nodes locally.',
    version='0.1',
    author='Nathan Wilcox',
    author_email='nejucomo+dev@gmail.com',
    license='GPLv3',
    url='https://github.com/nejucomo/{}'.format(PACKAGE),
    packages=find_packages(),
    install_requires=[
        'pathlib2 >= 2.3.0',
    ],

    entry_points={
        'console_scripts': [
            '{} = {}.main:main'.format(
                PACKAGE.replace('_', '-'),
                PACKAGE,
            )
        ],
    }
)
