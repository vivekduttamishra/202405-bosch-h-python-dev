from utils import normalize_arguments

def frequency(*values):
    
    values=normalize_arguments(values)   

    data={}
    for value in values:        
        if value in data:
            data[value]+=1
        else:
            data[value]=1

    return data