from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    requirement_list = []
    with open("requirements.txt",'r') as f:
        requirement_list = [line.rstrip() for line in f if not line.startswith('-e')]

    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Sarib",
    author_email="zama.sarib@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)
