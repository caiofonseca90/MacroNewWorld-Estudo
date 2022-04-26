from time import sleep, time
import keyboard as ky
import pyautogui as pg
import os
import string

def rodar():

    print(' -Seja Bem Vindo- ')
    print('\nDigite uma tecla esteja entre "A" e "Z" !!\n')

    lista = string.ascii_letters 
    tecla1 = str(input('Qual hotkey ira usar?: \n'))
    tempo = int(input('Quanto tempo de espera?: \n'))
    print('Você digitou...: ',tecla1)
   
    while True:
        if tecla1 in lista:
            try:
                contador = 0
                while contador <= 99999999:
                    print(' Para encerrar o programa basta apertar " CTRL + C " \n')            
                    pg.countdown(tempo)
                    ky.press(tecla1)
                    ky.release(tecla1)
                    contador = contador+1                
                    os.system('cls')
                    print('Você encheu o balde \033[1;31m{}\033[m vezes até o momento !!!'.format(contador))
                    sleep(0.4)
            except KeyboardInterrupt: 
 
                    print('\n \n \033[1;35mPrograma FINALIZADO\033[m  !!!')
                    contador = ''
                    sleep(1)
                    os.system('cls')
                    break


def continuar():
    print('Deseja retornar?\n Se \033[1;35mSIM\033[m aperte [1], caso \033[1;31mNÂO\033[m aperte [2] \n')
    
    opcao = int(input(''))
    while True:
        if opcao == 1:
            rodar()
            break
        if opcao == 2:
            os.system('cls')
            exit()    



rodar()
continuar()


