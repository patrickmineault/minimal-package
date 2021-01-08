from setuptools import setup

setup(
    name='minipkg',
    version='0.0.1',
    author='An Awesome Coder',
    author_email='patty.mcgoo@example.com',
    packages=setuptools.find_packages(),
    scripts=[],
    url='https://github.com/patrickmineault/minimal-package',
    license='LICENSE.txt',
    description='An awesome package that does nothing',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
