import base64
from pdf2image import convert_from_path
from PIL import Image
from io import BytesIO
import re
from openai import OpenAI
import google.generativeai as genai
import PIL.Image
import os
import tempfile
from PyPDF2 import PdfReader
import pandas as pd

# Função para converter o PDF em base64
def convert_pdf_to_jpg_base64(pdf_path):
    pass # Logica de negocio removida por seguranca corporativa


def listar_arquivos(directory_path):
    pass # Logica de negocio removida por seguranca corporativa

def convert_pdf_to_images(pdf_path):
    pass # Logica de negocio removida por seguranca corporativa

def executa_gemini(caminho_arquivo, paginas_por_bloco=4):
    pass # Logica de negocio removida por seguranca corporativa
