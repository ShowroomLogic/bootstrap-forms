import os
from setuptools import find_packages, setup
from bootstrap_forms import __version__, __author__, __author_email__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bootstrap-forms',
    version=__version__,
    description='Collection of templates for rendering django forms with Bootstrap markup.',
    url='https://github.com/ShowroomLogic/bootstrap-forms',
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    zip_safe=False
)
