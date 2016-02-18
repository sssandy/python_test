def normalize(name):
    result = name[0].upper()
    result +=  name[1:].lower()   
    return result    

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)    
