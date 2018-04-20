#!/usr/bin/env python
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
VERSION = open(os.path.join(here, 'VERSION')).read().strip()

install_requires = [
    # 'boto3' # install on own locally (pip instlal boto3) - lambda's containers already include this
]

setup(
    name='awsbase',
    version=VERSION,
    description="",
    author="mark mcclain",
    author_email='mjm461@gmail.com',
    url='',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    namespace_packages=['awsbase'],
    package_data={'awsbase': ['static/*.*', 'templates/*.*']},
    install_requires=install_requires,
    extras_require=dict(
        test=install_requires + [
            'pytest>=3.5',
        ],
        develop=install_requires + [
            'ipdb>=0.11',
        ]),
    zip_safe=False,
    entry_points={
        'console_scripts': [
        ],
    },
    dependency_links=[
    ],
)
