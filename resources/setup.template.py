from setuptools import setup
from sample import __version__, __author__

setup(name='sample',
      version=__version__,
      description='an example of python module',
      url='http://github.com/josanly/python-module-project',
      author=__author__,
      author_email='josso.adrien@gmail.com',
      license='GPL v3.0',
      packages=['sample'],
      python_requires='>=PYTHON_VERSION',
      zip_safe=False)

