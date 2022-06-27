import os
import shutil
import tkinter
import zipfile
import pyautogui as p
from tkinter import messagebox
import setup
import wget

#Verifica existencia de pasta temporaria para armazenagem da descompactacao
if not os.path.exists('C:\DesafioWindDigital\ArquivosDescompactados'):
    os.makedirs('C:\DesafioWindDigital\ArquivosDescompactados')


# DOWNLOAD AUTOMATICO
file_url = 'http://dados.tce.rs.gov.br/dados/licitacon/licitacao/ano/2022.csv.zip'
file = '2022.csv.zip'
wget.download(file_url)


#Faz a espera do download do arquivo .zip
while not os.path.isfile('2022.csv.zip'):
    p.sleep(1)
    if os.path.isfile('2022.csv.zip'):
        break


#Faz a extracao do arquivo .zip
with zipfile.ZipFile('2022.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\DesafioWindDigital\ArquivosDescompactados')

#Faz a movimentacao do itens necessarios para a pasta raiz
source_folder = r"C:\DesafioWindDigital\ArquivosDescompactados\\"
destination_folder = r"C:\DesafioWindDigital\\"
files_to_move = ['licitacao.csv', 'item.csv']

# iterate files
for file in files_to_move:
    # construct full file path
    source = source_folder + file
    destination = destination_folder + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)


#Apaga pasta temporaria
shutil.rmtree('C:\DesafioWindDigital\ArquivosDescompactados', ignore_errors=True)
os.remove('C:\DesafioWindDigital/2022.csv.zip')

#Chama Funcoes da biblioteca Teste.py
primeiras_linhas = setup.filtrar_linhas()
setup.gera_pastas(primeiras_linhas)

tkinter.messagebox.showinfo(title='Bot Desafio Wind Digital', message='Processo Concluido')