from distutils.core import setup
from setuptools import find_packages

with open('VERSION', 'r') as f:
    version = f.readline().strip()

with open('README.rst', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    install_requires = list()
    dependency_links = list()
    for line in f:
        re = line.strip()
        if re:
            if re.startswith('git+') or re.startswith('svn+') or re.startswith('hg+'):
                dependency_links.append(re)
            else:
                install_requires.append(re)

packages = find_packages()

setup(
    name='pyrallel.lib',
    version=version,
    packages=packages,
    url='https://github.com/usc-isi-i2/pyrallel',
    project_urls={
        "Bug Tracker": "https://github.com/usc-isi-i2/pyrallel/issues",
        "Documentation": "https://pyrallel.readthedocs.io",
        "Source Code": "https://github.com/usc-isi-i2/pyrallel",
    },
    license='MIT',
    author='USC/ISI',
    author_email='yixiangy@isi.edu',
    description='Yet another easy-to-use python3 parallel library for humans.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=(
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    )
)
