#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()\
                        .replace('.io/en/latest/', '.io/en/stable/')\
                        .replace('?badge=latest', '?badge=stable')\
                        .replace('projects/steam/badge/?version=latest', 'projects/steam/badge/?version=stable')
with open(path.join(here, 'steam/__init__.py'), encoding='utf-8') as f:
    __version__ = f.readline().split('"')[1]

# TODO: This should just pull from requirements.txt probably
install_requires = [
    'pycryptodomex>=3.21.0',
    'requests>=2.32.2',
    'cachetools>=5.5.2',
    'vdf @ git+https://github.com/solsticegamestudios/vdf.git@v4.0'
]

install_extras = {
    'client': [
        'gevent>=22.10',
        'protobuf~=5.29.3',
        'gevent-eventemitter~=2.1',
        'wsproto~=1.2.0'
    ],
}

setup(
    name='steam',
    version=__version__,
    description='Module for interacting with various Steam features',
    long_description=long_description,
    url='https://github.com/solsticegamestudios/steam',
    author="Rossen Georgiev / Solstice Game Studios",
    author_email='py-steam@solsticegamestudios.com',
    license='MIT',
    python_requires=">=3.8",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        #'Programming Language :: Python :: 3.13', # TODO: Test this works
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='valve steam steamid api webapi steamcommunity',
    packages=['steam'] + ['steam.'+x for x in find_packages(where='steam')],
    install_requires=install_requires,
    extras_require=install_extras,
    zip_safe=True,
)
