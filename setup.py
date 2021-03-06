#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from lockmyresource import __version__, __author__, __email__

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author=__author__,
    author_email=__email__,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Coordinate locking resources for humans and machines using a simple sqlite file.",
    entry_points={
        'console_scripts': [
            'lockmyresource=lockmyresource.cli:main',
            'lockmyresource-gui=lockmyresource.gui:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='lockmyresource',
    name='lockmyresource',
    packages=find_packages(include=['lockmyresource', 'lockmyresource.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/szabopeter/lockmyresource',
    version=__version__,
    zip_safe=False,
)
