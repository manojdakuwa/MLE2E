#Responsible for creating ML application as a package. and can be deply in pypi
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='ml_project',
    version='0.1.1',
    packages=find_packages(),
    author="Manoj",
    author_email="dakuwamanoj888@gmail.com",
    requires= get_requirement('requirement.txt')
)