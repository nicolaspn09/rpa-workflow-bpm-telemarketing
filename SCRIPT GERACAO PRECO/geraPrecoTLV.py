import os
import shutil
import locale
import requests
import cx_Oracle
import mysql.connector
import smtplib
import time
import pandas as pd
from datetime import datetime
from datetime import timedelta
from openpyxl import Workbook, load_workbook
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logExecucaoCodigos import grava_log_execucao_sql


#Converte as datas para serem utilizadas no restante do código
def converte_data():
    pass # Logica de negocio removida por seguranca corporativa

def handle_exception(e):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email_execucao():
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_oracle(query):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_oracle_insert(query):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql_insert(banco_dados, sql):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email(destinatarios, assunto, mensagem_email, diretorio_arquivo, cc=None, bcc=None):
    pass # Logica de negocio removida por seguranca corporativa

def envia_solicitacao_api(codigo_cliente, cnpj, codigo_ean):
    pass # Logica de negocio removida por seguranca corporativa

def gera_preco_api(codigo_cliente, cnpj, codigo_ean_lista):
    pass # Logica de negocio removida por seguranca corporativa

def consulta_itens_planilha(caminho_arquivo, caminho_arquivo_salvar):
    pass # Logica de negocio removida por seguranca corporativa

def consulta_pedidos():
    pass # Logica de negocio removida por seguranca corporativa

def executa_codigos():
    pass # Logica de negocio removida por seguranca corporativa

if __name__ == "__main__":
    #consulta_pedidos()
    retorno_api = gera_preco_api(codigo_cliente="454317", cnpj="35424485000125", codigo_ean_lista="7891150056572")
    retorno_api2 = gera_preco_api(codigo_cliente="121265", cnpj="5590137000167", codigo_ean_lista="7891150056572")
    print(retorno_api)
    print(retorno_api2)