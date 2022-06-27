import datetime
import os
import shutil
import pandas as pd

date_key = 'DT_ABERTURA'
parent_dir = r"C:\DesafioWindDigital\\"
name_dir = 'arquivos_gerados\\'

arquivosGerados = f'{parent_dir}{name_dir}'


#Apaga pasta "arquivos_gerados"
def delete_temp_files():
    shutil.rmtree(f'{parent_dir}{name_dir}')


#Filtra as 30 primeiras linhas, colocando as datas em ordem crescente
def filter_rows():
    df = pd.read_csv('licitacao.csv', date_parser=convert_date)
    filtered_df = df.loc[(df[date_key] >= '2022-05-01')].sort_values(date_key)
    firstRows = filtered_df.head(30)  # [:30]
    return firstRows


#Converte as datas CSV para o formato do Pandas
def convert_date(date):
    return datetime.datetime.strptime(str(date), '%d/%m/%Y')  # .strftime('%Y-%m-%d')


def filter_rows_items (row, items):
    orgao = row['CD_ORGAO']
    nrLicitacaoA = row['NR_LICITACAO']
    ano = row['ANO_LICITACAO']
    tipo = row['CD_TIPO_MODALIDADE']
    df_items_por_row = items.loc[(items['CD_ORGAO'] == orgao) & (items['NR_LICITACAO'] == nrLicitacaoA) & (items['ANO_LICITACAO'] == ano) & (items['CD_TIPO_MODALIDADE'] == tipo)]
    return df_items_por_row


#Gera as pastas, incluido os arquivos de textos com os links respectivos de cada licitacao
def generate_folders(firstRows):
    items = pd.read_csv('item.csv')
    for index, row in firstRows.iterrows():
        cdOrgao = row['CD_ORGAO']
        cdTipoModalidade = row['CD_TIPO_MODALIDADE']
        nrLicitacao = int(row['NR_LICITACAO'])
        anoLicitacao = row['ANO_LICITACAO']
        linkLicitacao = row['LINK_LICITACON_CIDADAO']

        path = f'{arquivosGerados}{cdOrgao} - {cdTipoModalidade} - {nrLicitacao} - {anoLicitacao}'
        link = 'link.txt'
        item_licitacoes = 'itens-licitacoes.csv'

        os.makedirs(f'{arquivosGerados}{cdOrgao} - {cdTipoModalidade} - {nrLicitacao} - {anoLicitacao}')
        arquivo = open(f'{path}\{link}', "a")
        arquivo.write(linkLicitacao)

        a = filter_rows_items(row ,items)
        a.to_csv(f'{path}\{item_licitacoes}', index_label='INDEX')