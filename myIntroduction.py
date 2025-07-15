from PyInquirer import prompt
from datetime import *


def chat():
    
    introduction = [
    {
        'type': 'input',
        'name': 'Intro',
        'message': 'Hello dear user who loves to document everything, can you please tell me your full name?',
        'validate': lambda val: val.strip() != '' or 'Ah dont be like that, please tell me your name',

    },
    ]
    
    print(f".....\n....\n...\nLet's create a readme file.\n")

    result = prompt(introduction)
    print(result)
    
    for key, value in result.items():
         print(f".....\n....\n...\nHello {value} let's create a readme file.\n")
         print(key)
         
         with open("README.md", "a") as f:
           #for key, value in introduction.items():
                today = datetime.today()
                f.write(f"Document Created by {value} on {today} \n\n---\n\n")
          
         