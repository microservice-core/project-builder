#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License'
} %}

setup(
    name='{{ project_slug }}',
    version='{{ version }}',
    description="{{ project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ author.replace('\"', '\\\"') }}",
    author_email='{{ email }}',
    url='https://github.com/{{ github_username }}/{{ project_slug }}',
    packages=[
        '{{ project_slug }}',
    ],
    package_dir={'{{ project_slug }}':
                 '{{ project_slug }}'},
    entry_points={
        'console_scripts': [
            '{{ project_name.replace(' ', '_')|lower }}=sources:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="{{ license }}",
    zip_safe=False,
    keywords='{{ project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        '{{ license_classifiers[open_source_license] }}',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
