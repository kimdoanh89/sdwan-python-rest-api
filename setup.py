from setuptools import setup

setup(
    name='sdwancli',
    version='0.1',
    py_modules=['sdwancli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sdwancli=vmanage.sdwancli:cli
    ''',
)
