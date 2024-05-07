from setuptools import find_packages,setup
# this will automatically find all the packages in the entire directory that we have created.
from typing import List

HYPHEN_E_DOT= '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
       requirements=file_obj.readlines()
       requirements=[req.replace("\n","")for req in requirements]
                                 
       if HYPHEN_E_DOT in requirements:
           requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
 name = 'mlproject',
 version = '0.0.1', #whenever you update next version can be given and uploaded in pypy
 author = 'Anand',
 author_email = 'anandmgupta04@gmail.com',
 packages=find_packages(), #it will check all the folders with __init.py and build it
 install_requires = get_requirements('requirements.txt')

)
