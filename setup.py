from setuptools import find_packages,setup

'''setup.py file is created so that our project can be turned into a installable package. setup.py is a file used in Python projects to define the metadata and 
 dependencies of the project. It is commonly used in conjunction with the setuptools package, which provides utilities for packaging, 
 distributing, and installing Python projects


 '''
Hyphen_E_Dot='-e.'
def get_requirement(file_path:str)->list[str]:
    with open(file_path) as file_obj: #The with statement is used to ensure that the file is properly closed after its suite finishes execution.
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements] #to omit the \n in the list 

        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)

    return requirements




setup(
name='ML Project',
version='0.0.1',
author='Javeria',
author_email='sjaverianadeem@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirements.txt') #to automatically get all the packages from 'requirement.txt' file
)