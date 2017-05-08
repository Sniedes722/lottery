from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lotterysystem',
    version='1.0.0',

    description='Coding Challenge for Greenphire',
    long_description=long_description,

    url='https://github.com/Sniedes722/lottery.git',

    author='Shawn Niederriter',
    author_email='shawnhitsback@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        
        'License :: OSI Approved :: MIT License',

        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    
    keywords='sample coding assignment',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages='lottery_system'
)
