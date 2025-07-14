from PyInquirer import prompt

def chat():
    
    introduction = [
    {
        'type': 'input',
        'name': 'Intro',
        'message': 'Hello user who loves to document everything, can you please tell me you name?',
    },
    ]
    
    result = prompt(introduction)
    
    for key, value in result.items(): #
         print(f"Hello {value} please answer the following questions to create a readme file.\n")
         
         