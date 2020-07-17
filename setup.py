  
from setuptools import setup, find_packages

setup(
	name='curiosity',
	version='0.0.1',
	license="MIT",
	description='See song stats to aid playlist curation',
	url="https://github.com/kabirvirji/curiosity",
    packages=find_packages(),
    install_requires=[],
    python_requires = ">= 3.4",
    author="Kabir Virji",
    author_email="kabirvirji@gmail.com",
    scripts=["curiosity"]
)
