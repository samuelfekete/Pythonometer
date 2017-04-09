
from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name='Pythonometer',
    version='0.1.0',
    description='A tool for measuring and improving Python skills',
    long_description=long_description,
    author='Samuel Fekete',
    packages=find_packages(),
    scripts=['native_app.py'],
    entry_points={
        'console_scripts': [
            'pythonometer=native_app:main'
        ]
    }
)
