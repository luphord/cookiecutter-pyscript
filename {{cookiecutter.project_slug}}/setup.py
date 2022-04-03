#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""{{cookiecutter.project_name}} setup script.
"""

from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}

setup(
    author='{{cookiecutter.full_name.replace("\"", "\\\"")}}',
    author_email="{{cookiecutter.email}}",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="""{{cookiecutter.project_short_description}}""",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}:main",
        ],
    },
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{cookiecutter.open_source_license}}",
{%- endif %}
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    data_files=[(".", ["LICENSE", "HISTORY.md"])],
    keywords="{{cookiecutter.project_slug}}",
    name="{{cookiecutter.project_slug}}",
    py_modules=["{{cookiecutter.project_slug}}"],
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    zip_safe=True,
)
