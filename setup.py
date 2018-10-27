from setuptools import find_packages, setup


setup(
    name='pycalc',
    version="1.0",
    description="pure python CLI calculator, python course home task",
    author="Dmitrii Pchelintsev",
    author_email="dmitrii_pchelintsev@epam.com",
    packages=find_packages(exclude=['tests']),
    entry_points={
        "console_scripts": [
            "pycalc=pycalc"
        ]
    }
)
