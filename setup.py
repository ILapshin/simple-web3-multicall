from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.1.5' 
DESCRIPTION = 'Simple Web3 multicall'

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='simple_multicall',
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Igor Lapshin',
    author_email= 'igorlapshin@list.ru',
    packages=find_packages(),
    license='MIT',
    keywords=['multicall', 'web3'],
    requires=['Web3'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ]
)
