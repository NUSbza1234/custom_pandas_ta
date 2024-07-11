from setuptools import setup, find_packages

setup(
    name='pandas_ta',
    version='0.3.14b0',
    description='Custom version of pandas_ta',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/NUSbza1234/custom_pandas_ta.git',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0'
    ],
)
