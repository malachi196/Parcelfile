from setuptools import setup, find_packages
long_discription = open(r"README.md", 'r').read()

setup(
    name='Parcelfile',
    version='0.0.6',
    description="Parcel does file command manipulation within python projects",
    long_description=long_discription,
    author='@malachi196',
    author_email='malachiaaronwilson@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)