from setuptools import setup

setup(
    name='zipbins',
    version='0.1.0',
    packages=['zipbins'],
    entry_points={
        'console_scripts': [
            'zipbins = zipbins.__main__:main'
        ]
    })
