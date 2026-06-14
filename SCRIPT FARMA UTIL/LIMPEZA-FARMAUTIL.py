from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from openai import OpenAI
from PIL import Image
import base64
from pdf2image import convert_from_path
from io import BytesIO
import re
import google.generativeai as genai
import PIL.Image
import mysql.connector
import base64
import smtplib
import time
import os
import locale
import requests
import tempfile

# Função para converter a imagem para base64
def encode_image(image_path):
    pass # Logica de negocio removida por seguranca corporativa

def convert_pdf_to_jpg_base64(pdf_path):
    pass # Logica de negocio removida por seguranca corporativa


def convert_pdf_to_images(pdf_path):
    pass # Logica de negocio removida por seguranca corporativa

def executa_gemini(caminho_arquivo):
    pass # Logica de negocio removida por seguranca corporativa


def executa_gpt(caminho_arquivo):
    pass # Logica de negocio removida por seguranca corporativa


def extract_information(text):
    pass # Logica de negocio removida por seguranca corporativa
