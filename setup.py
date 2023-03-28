#!/usr/bin/env python
# When a binary distribution is created for pyopencdms, the `opencdms`
# script created by the opencdms package is overwritten if pyopencdms
# is installed after opencdms.
# One workaround is to disable the creation of a binary distribution
# using `[global] no_binary=opencdms` in setup.cfg
# The alternative, used here, is to make the opencdms
# script created by pyopencdms import the same cli
# that the script created by opencdms would create.
"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.readlines()


setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="OpenCDMS",
    author_email="info@opencdms.org",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="OpenCDMS Python package",
    entry_points={
        "console_scripts": [
            "pyopencdms=pyopencdms.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="opencdms",
    name="pyopencdms",
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/opencdms-dev/pyopencdms",
    version="0.1.0",
    zip_safe=False,
)
