HYPEN_E_DOT = '-e .'
def get_requirments(file_path:str):
    '''
    This functions will return a list of requirments
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments

result = get_requirments('requirments.txt')
print(result)
