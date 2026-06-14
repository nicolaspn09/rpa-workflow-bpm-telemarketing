import tabula
import re
import os
import shutil
import pandas as pd
from PyPDF2 import PdfReader
from openpyxl import Workbook, load_workbook
import base64
from pdf2image import convert_from_path
from PIL import Image
from io import BytesIO
import google.generativeai as genai
import PIL.Image
import tempfile

class ProcessamentoArquivo:

    def __init__(self, caminho_arquivo):
        pass # Logica de negocio removida por seguranca corporativa


    def _extrair_texto_pdf(self):
        pass # Logica de negocio removida por seguranca corporativa


    def _ler_pdf_com_fallback(self):
        pass # Logica de negocio removida por seguranca corporativa


    def _extrair_tabela_manual(self):
        pass # Logica de negocio removida por seguranca corporativa


    def _extrair_informacoes_pdf(self):
        pass # Logica de negocio removida por seguranca corporativa


    def processar_tabelas(self):
        pass # Logica de negocio removida por seguranca corporativa


    def exec(self):
        pass # Logica de negocio removida por seguranca corporativa


    def convert_pdf_to_jpg_base64(self, pdf_path):
        pass # Logica de negocio removida por seguranca corporativa


    def listar_arquivos(self, directory_path):
        pass # Logica de negocio removida por seguranca corporativa


    def convert_pdf_to_images(self, pdf_path):
        pass # Logica de negocio removida por seguranca corporativa


    def executa_gemini(self, caminho_arquivo):
        pass # Logica de negocio removida por seguranca corporativa


    def processamento_arquivos(self):
        pass # Logica de negocio removida por seguranca corporativa


if __name__ == "__main__":
    #pdf_path = r"C:\Users\Nicolas\Downloads\BPM TLV\335511.pdf"
    pdf_path = r"C:\Users\Nicolas\Downloads\FARMA UTIL - 1 - 2024-07-26 16 55 00\374092.pdf"
    processador = ProcessamentoArquivo(pdf_path)
    infos_pdfs, qtd_itens = processador.processar_tabelas()
    processador.preencher_infos_excel(informacoes_pdf=infos_pdfs)
