from PyInquirer import prompt

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
        
with open("README.md", "a") as f:
    for key, value in answers.items(): #
         f.write(f"## {key}\n{value}\n")    
         
""" class QuestionsList:
    def __init__(self):
        self.objects = [{
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
       
 """