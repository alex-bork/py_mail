from setuptools import setup

setup(
    name='abork_mail',
    version='1.1.4', 
    packages=['py_mail'], 
    author='Alex Bork',
    license=open('LICENSE', 'r').read(),
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r', encoding="utf-8").read(),
)