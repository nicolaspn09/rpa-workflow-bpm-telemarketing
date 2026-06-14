from logExecucaoCodigos import grava_log_execucao_sql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from datetime import timedelta
import mysql.connector
import requests
import smtplib
import apiibm
import locale
import glob
import time
import os


#Envia e-mail para os usuários
def envia_email(mensagemEmail, destinatarios_email, assunto_email):    
    # Configurações do servidor SMTP
    smtp_server = 'mail.COMPANY_NAME.com.br'
    smtp_port = 25  # Porta para comunicação segura com TLS

    # Credenciais do remetente
    remetente_email = "rpa@COMPANY_NAME.com.br"
    remetente_senha = 'REMOVED_FOR_GITHUB'

    destinatarios = destinatarios_email
    #destinatarios = [destinatarios_enviar]

    # Crie uma mensagem MIMEMultipart
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente_email
    mensagem['To'] = ",".join(destinatarios)
    mensagem['Subject'] = assunto_email

    # Adicione o corpo do e-mail
    corpo_email = mensagemEmail
    mensagem.attach(MIMEText(corpo_email, 'html'))  # 'plain' para texto simples ou 'html' para HTML

    try:
        pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql(banco_dados, sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql_insert(banco_dados, sql):
    pass # Logica de negocio removida por seguranca corporativa

def verifica_sql():
    pass # Logica de negocio removida por seguranca corporativa

def rotina_principal_fila():
    pass # Logica de negocio removida por seguranca corporativa
