from setuptools import find_packages,setup
from typing import List
def get_requirments(file_path)->List[str]:
    reqirments=[]
    with open(file_path) as file_obj:
        reqirments=file_obj.readlines()
        reqirments=[req.replace('\n','') for req in reqirments]
        
        return reqirments
    

setup(
    name='dimondpriceprediction',
    author='sanjit',
    author_email='sanjitsaini059@gmail.com',
    install_requires=get_requirments('requirment.txt'),
    packages=find_packages()
)