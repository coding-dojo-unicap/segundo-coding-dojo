
def resultado(mao1,mao2):
    hashTable={'Pedra':['Tesoura','Largato'],'Papel':['Pedra','Spock'], 'Tesoura':['Papel', 'Largato']}
    play1 = 1
    play2 = 2
    empate = 0
    print('Mao1 :'+ mao1 + '\n' + 'Mao2: '+
    mao2)
    
    
    if(mao1 == mao2):
        return empate


    
    elif(mao1 == 'Pedra' and mao2 in hashTable[mao1]):
        return play1
    elif(mao1 == 'Pedra' and mao2 not in hashTable[mao1]):
        return play2
    elif(mao1 == 'Papel' and mao2 in hashTable[mao1]):
        return play1
    elif(mao1 == 'Papel' and mao2 not in hashTable[mao1]):
        return play2
    elif(mao1 == 'Tesoura' and mao2 in hashTable[mao1]):
        return play1
    elif(mao1 == 'Tesoura' and mao2 not in hashTable[mao1]):
        return play2

'''
    elif(mao1 == 'Papel' and mao2 == 'Tesoura'):
        return play2
    elif(mao1 == 'Papel' and mao2 == 'Spock'):
        return play1
    elif(mao1 == 'Papel' and mao2 == 'Lagarto'):
        return play2
'''
