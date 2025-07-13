#import PyInquirer
#import collections.abc
from PyInquirer import prompt
#from collections.abc import Mapping
# List of dictionaries questions[0-x]
questions = [
    {
        'type': 'input',
        'name': 'Project',
        'message': 'Project Title',
    },
    {
        'type': 'input',
        'name': 'Description',
        'message': 'Brief Description of the project',
    },
    {
        'type': 'input',
        'name': 'Install',
        'message': 'Provide installation instructions',
    },
    {
        'type': 'input',
        'name': 'Usage',
        'message': 'How to use',
    },
    {
        'type': 'list',
        'name': 'License',
        'message': 'Select a license',
        'choices': ['Yes', 'No', 'Maybe'],
    },
    {
        'type': 'input',
        'name': 'Contact',
        'message': 'Add contact information',
    },
]

answers = prompt(questions) # Place the answers from the quesion prompts into 
print (answers) #answers = {'Project': 'A', 'Description': 'B', 'Install': 'C', 'Usage': 'D', 'License': 'Yes', 'Contact': 'E'}
        
with open("readme-jb.txt", "a") as f:
    for key, value in answers.items(): #
         f.write(f"## {key}\n{value}\n")
        
