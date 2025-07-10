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
        'message': 'Do you like Python?',
        'default': True,
    }
]


# Could make this a module

answers = prompt(questions)
# add a loop here to go through the answers 
print(f"Project title is , {answers['title']}!")
