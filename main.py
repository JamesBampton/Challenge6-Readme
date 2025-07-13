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
]

# Could make this a module
answers = prompt(questions)
#qLength = len(answers)
#print(answers)
#print(qLength)
# add a loop here to go through the answers 
#print(f"Project title is , {answers['title']}!")
#print(f"Project description is , {answers['desc']}!")
    
        
for value in answers.values():
    
    
    
    
    
    
    #text = value
    with open("readme-jb.txt", "a") as f:
        #f.write(f"##{answers['title']}\n")
        f.write((str('##')))
        f.write(f"##{answers['title']}\n")
        f.write((str(value)))
        #f.write('\n')
        #f.write(text)
        
        #for key in answers.keys():
        #    f.write(f"# {key}\n")
        
