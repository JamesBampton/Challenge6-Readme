from PyInquirer import prompt
from rich.console import Console
from rich.prompt import Prompt # Cant get this to work - dont think it does for prompt values

console = Console()


def greet(name):
    console.print(f"\n[bold cyan]Thanks for your assistance, goodbye, [/bold cyan][bold red]{name}[/bold red]")


def myPrompt():
   
    questions = [
    {
        'type': 'input',
        'name': 'Project',
        'message': 'Project Title',
        'validate': lambda val: val.strip() != '' or 'This needs a value'
    },
    {
        'type': 'input',
        'name': 'Description',
        'message': 'Brief Description of the project',
        'validate': lambda val: val.strip() != '' or 'This needs a value'
    },
    {
        'type': 'input',
        'name': 'Install',
        'message': 'Provide installation instructions',
        'validate': lambda val: val.strip() != '' or 'This needs a value'
    },
    {
        'type': 'input',
        'name': 'Usage',
        'message': 'How to use',
        'validate': lambda val: val.strip() != '' or 'This needs a value'
    },
    {
        'type': 'list',
        'name': 'License',
        'message': 'Select a license',
        'choices': ['Windows', 'Linux', 'MSSQL', 'Apache', ' Tomcat', 'None'],
        'validate': lambda val: val.strip() != '' or 'This needs a value'
    },
    {
        'type': 'input',
        'name': 'Contact',
        'message': 'Add contact information',
        'validate': lambda val: val.strip() != '' or 'This needs a value'
    },
]   
           
    answers = prompt(questions) # Place the answers from the quesion prompts into 
    print (answers) #answers = {'Project': 'A', 'Description': 'B', 'Install': 'C', 'Usage': 'D', 'License': 'Yes', 'Contact': 'E'}
    with open("README.md", "a") as f:
        for key, value in answers.items():
            f.write(f"## {key}\n{value}\n\n---\n\n")
                  
