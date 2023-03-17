# to use it manualy type this in bash shell inside this file folder:
#
#sudo python setup.py build
#sync
#
#sudo python setup.py install_lib
#sync
#

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "AMPatio",
    version = "0.0.4",
    author = "Adir Vered",
    author_email = "adir.vrd@gmail.com",
    description = ("Clean & pure Python library for controlling & "
                   "manipulate digital IO pins on Amlogic SoC based boards"),
    license = "ISC",
    keywords = "AMLogic peripherals gpio",
    url = "https://github.com/adir-vrd/ampatio",
    packages=['AMPatio'],
    package_data={'AMPatio': ['boards/*', 'models/*/*']},
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: ISC License",
    ],
)
