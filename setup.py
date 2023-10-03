from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        # If -e . is found in requirements, the code proceeds to remove it from the list 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='icargo_project',
version='0.0.1',
URL='https://github.com/shum05/icargo.git',
License= 'MIT',
Keywords= 'machine learning, deep learning, NLP, computer vision',
Long_description = open("README.md", "r").read(),
author='Shum',
author_email='tshumetie5@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)