from setuptools import setup, find_packages

setup(
    name='libtest',
    version='0.1.0a1',
    install_requires=[
        'click',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'libtest=libtest.cli:cli',
        ],
    },
)
