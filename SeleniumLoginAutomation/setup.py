from setuptools import setup, find_packages

setup(
    name='selenium-login-automation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium~=4.20.0',
        'pytest~=8.2.0'
    ],
)