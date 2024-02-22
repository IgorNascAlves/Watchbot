import time
from time import strftime
from colorama import Fore, Back, Style, init
import os

# Initialize colorama
init(autoreset=True)

tempoinicio = time.time()
tempoanotado = tempoinicio
tecla = ""

cortes = 0
retomadas = 0
diferenca = 0
tempofinal = 0

def anotacorte(arquivo, tempoinicio):
        tempoanotado = round((time.time() - tempoinicio), 2)
        cortes = tempoanotado
        arquivo.write(strftime("%M:%S", time.gmtime(tempoanotado)) + "\tRed\tCorte")
        # print("Corte anotado em: " + strftime("%M:%S", time.gmtime(tempoanotado)) + "\n Adicione uma observação:")
        print(f'{Fore.GREEN}Corte anotado em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.RED}Adicione uma observação:{Style.RESET_ALL}')
        return cortes

def anotaretoma(arquivo, tempoinicio, cortes):
        tempoanotado = round((time.time() - tempoinicio), 2)
        retomadas = tempoanotado
        diferenca = retomadas - cortes
        # arquivo.write("Corte\t" + strftime("%M:%S", time.gmtime(cortes)) + '-' + strftime("%M:%S", time.gmtime(tempoanotado)))
        # arquivo.write("Retoma\t" + strftime("%M:%S", time.gmtime(tempoanotado)))
        arquivo.write(strftime("%M:%S", time.gmtime(tempoanotado)) + "\tRed\tCorte")
        # print(f'{Fore.GREEN}Retoma em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.RED}Adicione uma observação:{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Retoma em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.BLUE}Tempo de corte: {strftime("%M:%S", time.gmtime(diferenca))}{Style.RESET_ALL}\n{Fore.RED}Adicione uma observação:{Style.RESET_ALL}')
        return diferenca

def anotazoom(arquivo, tempoinicio):
        tempoanotado = round((time.time() - tempoinicio), 2)
        arquivo.write(strftime("%M:%S", time.gmtime(tempoanotado)) + "\tRose\tDestaque")
        print(f'{Fore.GREEN}Destaque anotado em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.RED}Adicione uma observação:{Style.RESET_ALL}')

def anotatopicos(arquivo, tempoinicio):
        tempoanotado = round((time.time() - tempoinicio), 2)
        arquivo.write(strftime("%M:%S", time.gmtime(tempoanotado)) + "\tGreen\tTópicos")
        print(f'{Fore.GREEN}Tópico anotado em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.RED}Adicione uma observação:{Style.RESET_ALL}')

def anotaLT(arquivo, tempoinicio):
        tempoanotado = round((time.time() - tempoinicio), 2)
        arquivo.write(strftime("%M:%S", time.gmtime(tempoanotado)) + "\tBlue\tLettering")
        print(f'{Fore.GREEN}Lettering anotado em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.RED}Adicione uma observação:{Style.RESET_ALL}')

def anotainsert(arquivo, tempoinicio):
        tempoanotado = round((time.time() - tempoinicio), 2)
        arquivo.write(strftime("%M:%S", time.gmtime(tempoanotado)) + "\tYellow\tInserção")
        print(f'{Fore.GREEN}Insert anotado em: {strftime("%M:%S", time.gmtime(tempoanotado))}\n {Fore.RED}Adicione uma observação:{Style.RESET_ALL}')

def mostratempo(tempoinicio, diferenca):
        tempoanotado = round((time.time() - tempoinicio), 2)
        print(f'{Fore.WHITE}Tempo atual de vídeo: {strftime("%M:%S", time.gmtime(tempoanotado))}\n{Style.RESET_ALL}')
        tempofinal = tempoanotado - diferenca
        print(f'{Fore.GREEN}Tempo final estimado com cortes\t {strftime("%M:%S", time.gmtime(tempofinal))}{Style.RESET_ALL}')

def terminavideo(arquivo, tempoinicio, diferenca):
        tempoanotado = round((time.time() - tempoinicio), 2)
        tempofinal = tempoanotado - diferenca
        arquivo.write("Tempo total de vídeo\t" + strftime("%M:%S", time.gmtime(tempoanotado)))
        arquivo.write("\n" + "Tempo final estimado com cortes\t" + strftime("%M:%S", time.gmtime(tempofinal)))


print (f"{Fore.YELLOW}S-Inicia contagem C-corte V-retoma I-insert D-destaque T-topicos L-lettering M-Tempo Atual Q-fechar\ninsira o comando e confirme com Enter, em seguida, você pode adicionar uma observação e apertar Enter novamente para completar a anotação{Style.RESET_ALL}")


id_curso = input("Informe o id do curso: ")
num_video = input("Informe o número do vídeo: ")

with open(f"{id_curso}-{num_video}.txt", "w", encoding='utf-8') as arquivo:
        comandos = ["c", "d", "l", "q", "i", "v", "t", "s", "m"]
        while True:

            
            tecla = input(f"{Fore.YELLOW}\nInsira o comando:\nS-Inicia contagem C-corte V-retoma I-insert D-destaque T-topicos L-lettering M-Tempo Atual Q-fechar\n{Style.RESET_ALL}").lower()
            

            if tecla in comandos:
                  match tecla:
                          case "s":
                                        tempoinicio = time.time()
                                        print("Cronometro reiniciado ")
                                        # arquivo.write("Inicio do vídeo: " + strftime("%M:%S", time.gmtime(tempoinicio)) + "\n")
                          case "c":
                                        cortes = anotacorte(arquivo, tempoinicio)
                                        arquivo.write("\t"+input()+"\n")
                          case "v":
                                        diferenca += anotaretoma(arquivo, tempoinicio, cortes)
                                        arquivo.write("\tRetoma ")
                                        arquivo.write(input()+"\n")
                          case "l":
                                        anotaLT(arquivo, tempoinicio)
                                        arquivo.write("\t"+input()+"\n")
                          case "d":
                                        anotazoom(arquivo, tempoinicio)
                                        arquivo.write("\t"+input()+"\n")
                          case "i":
                                        anotainsert(arquivo, tempoinicio)
                                        arquivo.write("\t"+input()+"\n")
                          case "t":
                                        anotatopicos(arquivo, tempoinicio)
                                        arquivo.write("\t"+input()+"\n")
                          case "q":
                                        terminavideo(arquivo, tempoinicio, diferenca)
                                        print ("\nFim da anotação")
                                        mostratempo(tempoinicio, diferenca)
                                        ## use system pause
                                        break
                          case "m":
                                        mostratempo(tempoinicio, diferenca)
                          case _:
                                        print("\nErro\n")
            else:
                  
                  print(f"{Fore.RED}\nCOMANDO INEXISTENTE\n{Style.RESET_ALL}")
                  
os.system("pause")