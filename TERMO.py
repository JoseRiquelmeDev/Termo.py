import random
from copy import deepcopy
# Define variaveis principais
vocabulario = []
with open('br-sem-acentos.txt', 'r') as arquivo:
    VocabularioTotal = [linha.strip() for linha in arquivo.readlines()]
for c in VocabularioTotal:
    if len(c) == 5:
        vocabulario.append(c)
tentativas = 0
palavra = list(''.join(random.sample(vocabulario, 1)).upper())
# INICIO DO JOGO
print('-='*10)
print('{:^20}'.format('TERMO.PY'))
print('-='*10)
print('CASO NÃO SAIBA AS REGRAS DIGITE 1 ')
while True:
    temporario = deepcopy(palavra)
    user = input('\n\033[mDIGITE UMA PALAVRA DE 5 LETRAS: ').strip().upper()
    # Checa se o usuario usou uma palavra válida
    if user == '1':
        print('''
Olá e Bem-vindo ao termo.py, uma versão em python do jogo Termo
Seu objetivo é descobrir a palavra correta, depois da primeira
tentativa a cor das letras pode te dar algumas dicas...
        
- Se a letra é \033[31mVERMELHA\033[m, significa que essa letra não está na palavra.
- Se a letra é \033[33mAMARELA\033[m, significa que essa letra está na palavra, porém
na posição errada.
- Se a letra é \033[32mVERDE\033[m, significa que essa letra está na posição correta!''')
    elif len(user) != 5:
        print('PALAVRA INVALIDA, TENTE NOVAMENTE: ')
    # Checa letra por letra se estão corretas
    else:
        tentativas += 1
        for pos in range(0, 5):
            if user[pos] == palavra[pos]:
                print('\033[32m', user[pos], end='')
            elif user[pos] in palavra and user[pos] in temporario:
                for c in range(0, 5):
                    if user[c] == palavra[c] and user[c] in temporario:
                        temporario.remove(user[c])
                if user[pos] in temporario:
                    temporario.remove(user[pos])
                    print('\033[33m', user[pos], end='')
                else:
                    print('\033[31m', user[pos], end='')
            else:
                print('\033[31m', user[pos], end='')
        # Define se o usuario acertou
        if palavra == list(user):
            print('\nVOCÊ ACERTOU! PARABÉNS! A PALAVRA ERA: \033[32m{}\033[m'.format(''.join(palavra)))
            break
        # Checa se o usuario perdeu
        else:
            print(f'\n\033[36mVocê tem {6 - tentativas} tentativas')
            if tentativas >= 6:
                print('\033[31mVOCÊ PERDEU! A PALAVRA ERA: \033[31m{}\033[m'.format(''.join(palavra)))
                break
