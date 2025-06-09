from setuptools import find_packages , setup

from typing import List

def get_reqirements()-> List[str]:
    """
    This function will return the list of requirements
    """
    with open('requirements.txt' ,'r') as f:
        requirements = f.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements