from PyInquirer import prompt

def chat():
    
    introduction = [
    {
        'type': 'input',
        'name': 'Intro',
        'message': 'Hello dear user who loves to document everything, can you please tell me your name?',
        'validate': lambda val: val.strip() != '' or 'Ah dont be like that, please tell me your name',

    },
    ]
    
    print(f".....\n....\n...\nLet's create a readme file.\n")

    result = prompt(introduction)
    
    for key, value in result.items():
         print(f".....\n....\n...\nHello {value} let's create a readme file.\n")
         print(key)
         
         