#import PyInquirer
#import collections.abc
from PyInquirer import prompt
#from collections.abc import Mapping

questions = [
    {
        'type': 'input',
        'name': 'title',
        'message': 'Project Title',
    },
    {
        'type': 'input',
        'name': 'desc',
        'message': 'Brief Description of the project',
    },
    {
        'type': 'input',
        'name': 'install',
        'message': 'Provide installation instructions',
    },
    {
        'type': 'input',
        'name': 'usage',
        'message': 'How to use',
    },
    {
        'type': 'list',
        'name': 'license',
        'message': 'Select a license',
        'choices': ['Yes', 'No', 'Maybe'],
    },
    {
        'type': 'input',
        'name': 'contact',
        'message': 'Add contact information',
    },
    {
        'type': 'confirm',
        'name': 'confirm',
        'message': 'Save File?',
        'default': True,
    }
]


# Could make this a module

answers = prompt(questions)
qLength = len(answers)
print(answers)
print(qLength)
# add a loop here to go through the answers 
print(f"Project title is , {answers['title']}!")

with open("readme-jb.txt", "w") as f:
        f.write(str(answers))


""" i=0
for i in answers:
    with open("readme-jb.txt", "w") as f:
        f.write([answers['title']])
    
    with open("readme-jb.md", "w") as f:
        f.write([answers['title']]) """
    
