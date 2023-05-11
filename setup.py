from setuptools import setup,find_packages

#this method is the feature to be included when made public, name, version ,and its attributes basically...
setup(
    name = "mypackage",
    version = "0.1",
    packages = find_packages(exclude = ['tests*']),
    license = "MIT",
    description = 'EDSA example python package',
    long_desc = open('README.md').read(),
    intall_requires = ['numpy'],
    url ='https://girhub.com/.....',
    author = 'Phelelani Mkhize'
)

