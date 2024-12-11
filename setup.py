from setuptools import setup,find_packages
from typing import List

def get_requiements()->list[str]:
    requiements_list=list[str] =[]
    
    return requiements_list 
    


setup(
    name ="sensor",
    version="0.0.1",
    author= 'shubham',
    author_email="shubhammokal30@gmail.com",
    packages=find_packages(),
    install_requires =get_requiements(),
)

